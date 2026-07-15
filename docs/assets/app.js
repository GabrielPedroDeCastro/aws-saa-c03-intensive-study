(() => {
  "use strict";

  const dataNode = document.querySelector("#site-data");
  if (!dataNode) return;
  const site = JSON.parse(dataNode.textContent);
  const storageKey = "aws-saa-c03-portal-v1";
  const emptyState = {
    theme: null,
    labs: [],
    activePlan: "4-semanas",
    planDays: {},
    quiz: { started: false, index: 0, answers: [], finished: false },
  };

  function loadState() {
    try {
      const saved = JSON.parse(localStorage.getItem(storageKey) || "{}");
      return {
        ...emptyState,
        ...saved,
        labs: Array.isArray(saved.labs) ? saved.labs : [],
        planDays: saved.planDays || {},
        quiz: { ...emptyState.quiz, ...(saved.quiz || {}) },
      };
    } catch (_) {
      return structuredClone(emptyState);
    }
  }

  let state = loadState();
  let selectedDomain = "all";

  function saveState() {
    try { localStorage.setItem(storageKey, JSON.stringify(state)); } catch (_) { /* storage can be disabled */ }
  }

  const escapeHtml = (value) => String(value)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#039;");

  const normalize = (value) => String(value).normalize("NFD").replace(/[\u0300-\u036f]/g, "").toLowerCase();

  function setTheme(theme) {
    const effective = theme || (matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light");
    document.documentElement.dataset.theme = effective;
    const button = document.querySelector("[data-theme-toggle]");
    if (button) {
      button.textContent = effective === "dark" ? "☀" : "☾";
      button.setAttribute("aria-label", effective === "dark" ? "Usar tema claro" : "Usar tema escuro");
    }
  }

  function initNavigation() {
    const menuButton = document.querySelector("[data-menu-toggle]");
    const menu = document.querySelector("[data-menu]");
    menuButton?.addEventListener("click", () => {
      const open = menu.classList.toggle("open");
      menuButton.setAttribute("aria-expanded", String(open));
    });
    menu?.querySelectorAll("a").forEach((link) => link.addEventListener("click", () => {
      menu.classList.remove("open");
      menuButton?.setAttribute("aria-expanded", "false");
    }));
    document.querySelector("[data-theme-toggle]")?.addEventListener("click", () => {
      state.theme = document.documentElement.dataset.theme === "dark" ? "light" : "dark";
      setTheme(state.theme);
      saveState();
    });

    const links = [...document.querySelectorAll(".main-nav a")];
    const sections = links.map((link) => document.querySelector(link.getAttribute("href"))).filter(Boolean);
    if ("IntersectionObserver" in window) {
      const observer = new IntersectionObserver((entries) => {
        const visible = entries.filter((entry) => entry.isIntersecting).sort((a, b) => b.intersectionRatio - a.intersectionRatio)[0];
        if (!visible) return;
        links.forEach((link) => link.toggleAttribute("aria-current", link.getAttribute("href") === `#${visible.target.id}`));
      }, { rootMargin: "-25% 0px -65%", threshold: [0, .2, .5] });
      sections.forEach((section) => observer.observe(section));
    }
  }

  function renderStats() {
    const labels = [
      [site.stats.domains, "domínios oficiais"],
      [site.stats.topics, "tópicos decisórios"],
      [site.stats.labs, "labs completos"],
      [site.stats.questions, "questões autorais"],
      [site.stats.flashcards, "flashcards"],
      [site.stats.mockExams, "simulados completos"],
    ];
    document.querySelector("[data-stats]").innerHTML = labels.map(([value, label]) =>
      `<div class="stat"><strong>${value}</strong><span>${escapeHtml(label)}</span></div>`
    ).join("");
  }

  function topicRows() {
    return site.topics.domains.flatMap((domain) => domain.topics.map((topic) => ({ domain, topic })));
  }

  function renderGuide() {
    const filters = document.querySelector("[data-domain-filters]");
    const overview = document.querySelector("[data-domain-overview]");
    filters.innerHTML = [
      `<button class="filter-button" type="button" data-domain="all" aria-pressed="true">Todos</button>`,
      ...site.topics.domains.map((domain) => `<button class="filter-button" type="button" data-domain="${domain.id}" aria-pressed="false">${domain.id} · ${domain.weight}%</button>`),
    ].join("");
    overview.innerHTML = site.topics.domains.map((domain) => `
      <article class="domain-chip">
        <span><b>${domain.id}</b><b>${domain.weight}%</b></span>
        <strong>${escapeHtml(domain.title)}</strong>
        <div class="domain-bar"><i style="width:${domain.weight * 3.1}%"></i></div>
      </article>`).join("");

    filters.addEventListener("click", (event) => {
      const button = event.target.closest("[data-domain]");
      if (!button) return;
      selectedDomain = button.dataset.domain;
      filters.querySelectorAll("button").forEach((item) => item.setAttribute("aria-pressed", String(item === button)));
      filterTopics();
    });
    document.querySelector("[data-topic-search]").addEventListener("input", filterTopics);
    filterTopics();
  }

  function filterTopics() {
    const query = normalize(document.querySelector("[data-topic-search]").value.trim());
    const rows = topicRows().filter(({ domain, topic }) => {
      const inDomain = selectedDomain === "all" || selectedDomain === domain.id;
      const text = normalize([topic.title, topic.technical, topic.child, topic.when, topic.limits, topic.traps].join(" "));
      return inDomain && (!query || text.includes(query));
    });
    const grid = document.querySelector("[data-topic-grid]");
    grid.innerHTML = rows.map(({ domain, topic }) => {
      const links = topic.links.map((url, index) => `<a href="${escapeHtml(url)}" target="_blank" rel="noreferrer">AWS ${index + 1} ↗</a>`).join("");
      return `<details class="topic-card">
        <summary><span class="domain-tag">${domain.id}</span><h3>${escapeHtml(topic.title)}</h3><span class="expand-mark" aria-hidden="true">+</span></summary>
        <div class="topic-body">
          <p><b>Técnico.</b> ${escapeHtml(topic.technical)}</p>
          <p class="kid-note"><b>Como criança.</b> ${escapeHtml(topic.child)}</p>
          <div class="topic-meta"><div><span>Quando usar</span>${escapeHtml(topic.when)}</div><div><span>Limitações</span>${escapeHtml(topic.limits)}</div><div><span>Custo</span>${escapeHtml(topic.cost)}</div><div><span>Pegadinha</span>${escapeHtml(topic.traps)}</div></div>
          <div class="topic-links">${links}</div>
        </div>
      </details>`;
    }).join("");
    document.querySelector("[data-topic-empty]").hidden = rows.length > 0;
  }

  function renderLabs() {
    const grid = document.querySelector("[data-lab-grid]");
    grid.innerHTML = site.labs.map((lab) => `
      <article class="lab-card">
        <div class="lab-image"><img src="diagrams/${escapeHtml(lab.diagram)}" alt="Diagrama do lab ${escapeHtml(lab.title)}" loading="lazy"></div>
        <div class="lab-content">
          <div class="lab-topline"><span>Lab ${lab.number} · ${lab.domain}</span><span>${lab.minutes} min · ${escapeHtml(lab.cost)}</span></div>
          <h3>${escapeHtml(lab.title)}</h3><p>${escapeHtml(lab.summary)}</p>
          <div class="lab-actions"><a href="${escapeHtml(lab.url)}" target="_blank" rel="noreferrer">Abrir roteiro ↗</a>
            <label class="check-control"><input type="checkbox" data-lab-check="${lab.id}" ${state.labs.includes(lab.id) ? "checked" : ""}><span>Concluído</span></label>
          </div>
        </div>
      </article>`).join("");
    grid.addEventListener("change", (event) => {
      const input = event.target.closest("[data-lab-check]");
      if (!input) return;
      state.labs = input.checked ? [...new Set([...state.labs, input.dataset.labCheck])] : state.labs.filter((id) => id !== input.dataset.labCheck);
      saveState();
      updateLabProgress();
    });
    updateLabProgress();
  }

  function updateLabProgress() {
    const completed = state.labs.filter((id) => site.labs.some((lab) => lab.id === id)).length;
    document.querySelector("[data-lab-progress-label]").textContent = `${completed} de ${site.labs.length} concluídos`;
    document.querySelector("[data-lab-progress]").style.width = `${completed / site.labs.length * 100}%`;
  }

  function renderPlans() {
    const planGrid = document.querySelector("[data-plan-grid]");
    planGrid.innerHTML = site.plans.map((plan) => `<button class="plan-card ${state.activePlan === plan.id ? "active" : ""}" type="button" data-plan="${plan.id}"><span>${escapeHtml(plan.label)}</span><strong>${escapeHtml(plan.title)}</strong><small>${escapeHtml(plan.pace)}</small><p>${escapeHtml(plan.description)}</p></button>`).join("");
    planGrid.onclick = (event) => {
      const button = event.target.closest("[data-plan]");
      if (!button) return;
      state.activePlan = button.dataset.plan;
      saveState();
      renderPlans();
    };
    const plan = site.plans.find((item) => item.id === state.activePlan) || site.plans[0];
    document.querySelector("[data-active-plan-title]").textContent = `${plan.title} · ${plan.pace}`;
    const planDays = state.planDays[plan.id] || [];
    const grid = document.querySelector("[data-day-grid]");
    grid.innerHTML = Array.from({ length: plan.days }, (_, index) => {
      const day = index + 1;
      return `<label class="day-check"><input type="checkbox" value="${day}" ${planDays.includes(day) ? "checked" : ""}><span>Dia</span><strong>${String(day).padStart(2, "0")}</strong></label>`;
    }).join("");
    grid.onchange = (event) => {
      const day = Number(event.target.value);
      const current = state.planDays[plan.id] || [];
      state.planDays[plan.id] = event.target.checked ? [...new Set([...current, day])] : current.filter((item) => item !== day);
      saveState();
      updatePlanProgress(plan);
    };
    updatePlanProgress(plan);
  }

  function updatePlanProgress(plan) {
    const done = (state.planDays[plan.id] || []).length;
    const percent = Math.round(done / plan.days * 100);
    document.querySelector("[data-plan-progress-label]").textContent = `${percent}%`;
    document.querySelector("[data-plan-progress]").style.width = `${percent}%`;
  }

  const questions = site.quiz.questoes;

  function renderQuizDots() {
    const dots = document.querySelector("[data-question-dots]");
    dots.innerHTML = questions.map((question, index) => {
      const answer = state.quiz.answers[index];
      let status = index === state.quiz.index && state.quiz.started && !state.quiz.finished ? "current" : "";
      if (answer) status = answer.correct ? "correct" : "wrong";
      return `<span class="question-dot ${status}" title="Questão ${index + 1}"></span>`;
    }).join("");
    const answered = state.quiz.answers.filter(Boolean);
    const correct = answered.filter((answer) => answer.correct).length;
    document.querySelector("[data-quiz-score]").textContent = answered.length ? `${correct}/${answered.length}` : "—";
    document.querySelector("[data-quiz-score-label]").textContent = state.quiz.finished ? `${Math.round(correct / questions.length * 100)}% de acerto` : `${answered.length} de ${questions.length} respondidas`;
  }

  function renderQuiz() {
    const start = document.querySelector("[data-quiz-start]");
    const questionPanel = document.querySelector("[data-quiz-question]");
    const result = document.querySelector("[data-quiz-result]");
    start.hidden = state.quiz.started || state.quiz.finished;
    questionPanel.hidden = !state.quiz.started || state.quiz.finished;
    result.hidden = !state.quiz.finished;
    renderQuizDots();
    if (state.quiz.finished) {
      const correct = state.quiz.answers.filter((answer) => answer?.correct).length;
      const percent = Math.round(correct / questions.length * 100);
      result.innerHTML = `<span class="quiz-badge">Tentativa concluída</span><h3>${percent >= 80 ? "Base firme para avançar." : "Agora você sabe onde atacar."}</h3><p>Você acertou <b>${correct} de ${questions.length}</b> questões (${percent}%). ${percent >= 80 ? "Siga para o Lab 01 e explique cada rota antes do deploy." : "Revise os feedbacks, desenhe uma VPC em duas AZs e tente novamente em D+1."}</p><button class="button button-primary" type="button" data-result-reset>Fazer nova tentativa</button>`;
      result.querySelector("[data-result-reset]").addEventListener("click", resetQuiz);
      return;
    }
    if (state.quiz.started) renderQuestion();
  }

  function renderQuestion() {
    const index = Math.min(state.quiz.index, questions.length - 1);
    const question = questions[index];
    const recorded = state.quiz.answers[index];
    const panel = document.querySelector("[data-quiz-question]");
    const options = Object.entries(question.alternativas).map(([letter, label]) => {
      let status = "";
      if (recorded && letter === question.resposta_correta) status = "correct";
      if (recorded && letter === recorded.answer && !recorded.correct) status = "wrong";
      return `<button class="option-button ${status}" type="button" data-answer="${letter}" ${recorded ? "disabled" : ""}><span class="option-letter">${letter}</span><span>${escapeHtml(label)}</span></button>`;
    }).join("");
    const feedback = recorded ? `<div class="feedback-panel ${recorded.correct ? "" : "wrong"}" role="status"><h4>${recorded.correct ? "Acertou. Boa decisão." : `A melhor resposta é ${question.resposta_correta}.`}</h4><p>${escapeHtml(recorded.correct ? question.feedback_acerto : question.feedback_erro)}</p><p><b>Como criança:</b> ${escapeHtml(question.explicacao_crianca)}</p><details><summary>Ver explicação de todas as alternativas</summary>${Object.entries(question.explicacao_alternativas).map(([letter, text]) => `<p><b>${letter}.</b> ${escapeHtml(text)}</p>`).join("")}</details><div class="feedback-actions"><button class="button button-primary" type="button" data-next>${index === questions.length - 1 ? "Ver resultado" : "Próxima questão"}</button></div></div>` : "";
    panel.innerHTML = `<div class="question-meta"><span>Questão ${index + 1} de ${questions.length}</span><span>${escapeHtml(question.codigo_dominio)} · ${escapeHtml(question.dificuldade)} · ${question.tempo_sugerido_segundos}s</span></div><h3>${escapeHtml(question.topico)}</h3><p class="question-prompt">${escapeHtml(question.enunciado)}</p><div class="option-list">${options}</div>${feedback}`;
    panel.querySelectorAll("[data-answer]").forEach((button) => button.addEventListener("click", () => answerQuestion(button.dataset.answer)));
    panel.querySelector("[data-next]")?.addEventListener("click", nextQuestion);
  }

  function answerQuestion(answer) {
    const index = state.quiz.index;
    if (state.quiz.answers[index]) return;
    state.quiz.answers[index] = { answer, correct: answer === questions[index].resposta_correta };
    saveState();
    renderQuiz();
  }

  function nextQuestion() {
    if (state.quiz.index >= questions.length - 1) {
      state.quiz.finished = true;
      state.quiz.started = false;
    } else {
      state.quiz.index += 1;
    }
    saveState();
    renderQuiz();
    document.querySelector("[data-quiz-card]").scrollIntoView({ behavior: "smooth", block: "center" });
  }

  function resetQuiz() {
    state.quiz = { started: true, index: 0, answers: [], finished: false };
    saveState();
    renderQuiz();
  }

  function initQuiz() {
    document.querySelector("[data-quiz-begin]").addEventListener("click", () => {
      state.quiz.started = true;
      state.quiz.finished = false;
      saveState();
      renderQuiz();
    });
    document.querySelector("[data-quiz-reset]").addEventListener("click", resetQuiz);
    renderQuiz();
  }

  setTheme(state.theme);
  initNavigation();
  renderStats();
  renderGuide();
  renderLabs();
  renderPlans();
  initQuiz();
})();
