(() => {
  const root = document.documentElement;
  const body = document.body;
  const base = body.dataset.root || ".";
  const page = body.dataset.page || "";
  const storageKey = "nishita-journal-theme";

  const navItems = [
    { id: "home", href: `${base}/index.html`, label: "Home" },
    { id: "journal", href: `${base}/journal/index.html`, label: "Journal" },
    { id: "progress", href: `${base}/progress.html`, label: "Progress" },
    { id: "future", href: `${base}/future.html`, label: "Future" },
    { id: "about", href: `${base}/about.html`, label: "About" },
    { id: "contact", href: `${base}/contact.html`, label: "Contact" },
  ];

  const weekNav = [
    { id: "community-bonding", href: `${base}/journal/community-bonding.html`, label: "Bonding" },
    ...Array.from({ length: 12 }, (_, i) => ({
      id: `week-${i + 1}`,
      href: `${base}/journal/week-${i + 1}.html`,
      label: `Week ${i + 1}`,
    })),
    { id: "final-submission", href: `${base}/journal/final-submission.html`, label: "Final" },
    { id: "end-term", href: `${base}/journal/end-term.html`, label: "End term" },
  ];

  const applyTheme = (mode) => {
    root.dataset.theme = mode;
    localStorage.setItem(storageKey, mode);
    const toggle = document.querySelector("[data-theme-toggle]");
    if (toggle) {
      toggle.setAttribute("aria-checked", mode === "dark" ? "true" : "false");
      toggle.setAttribute("title", mode === "dark" ? "Switch to light mode" : "Switch to dark mode");
    }
  };

  const saved = localStorage.getItem(storageKey);
  applyTheme(saved === "dark" || saved === "light" ? saved : "light");

  const header = document.createElement("header");
  header.className = "site-header";
  header.innerHTML = `
    <nav class="navbar" aria-label="Primary">
      <a class="brand" href="${base}/index.html">
        <img src="${base}/assets/favicon.svg" alt="" width="26" height="26">
        <span>NISHITA SHAH</span>
      </a>
      <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="site-nav" aria-label="Open menu">
        <span></span><span></span>
      </button>
      <div class="nav-cluster" id="site-nav">
        <ul class="nav-links">
          ${navItems
            .map(
              (item) => `
            <li>
              <a class="nav-link${page === item.id || (item.id === "journal" && page.startsWith("journal")) ? " active" : ""}" href="${item.href}">${item.label}</a>
            </li>`
            )
            .join("")}
        </ul>
        <div class="nav-tools">
          <a class="icon-link" href="https://github.com/Nishita-shah1" target="_blank" rel="noopener noreferrer" aria-label="GitHub profile">
            <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true"><path fill="currentColor" d="M12 .5A11.5 11.5 0 0 0 .5 12.7c0 5.4 3.4 10 8.2 11.6.6.1.8-.3.8-.6v-2.1c-3.3.7-4-1.6-4-1.6-.5-1.3-1.2-1.7-1.2-1.7-1-.7.1-.7.1-.7 1.1.1 1.7 1.2 1.7 1.2 1 .1.8 1.8 2.8 1.3.1-.8.4-1.3.7-1.6-2.7-.3-5.5-1.4-5.5-6.1 0-1.3.5-2.4 1.2-3.3-.1-.3-.5-1.6.1-3.3 0 0 1-.3 3.4 1.2a11.4 11.4 0 0 1 6.2 0c2.3-1.5 3.3-1.2 3.3-1.2.7 1.7.3 3 .2 3.3.8.9 1.2 2 1.2 3.3 0 4.7-2.8 5.8-5.5 6.1.4.4.8 1.1.8 2.2v3.2c0 .3.2.7.8.6 4.8-1.6 8.2-6.2 8.2-11.6A11.5 11.5 0 0 0 12 .5Z"/></svg>
          </a>
          <button class="theme-switch" type="button" data-theme-toggle role="switch" aria-checked="${root.dataset.theme === "dark"}" title="Toggle dark mode">
            <span class="theme-switch-icon" aria-hidden="true">☀</span>
            <span class="theme-switch-icon" aria-hidden="true">☾</span>
            <span class="theme-switch-thumb"></span>
          </button>
        </div>
      </div>
    </nav>
  `;
  body.prepend(header);

  const footer = document.createElement("footer");
  footer.className = "site-footer";
  footer.innerHTML = `
    <p>Nishita Shah · Google Summer of Code 2026</p>
    <p>Built as a public engineering journal for Animint2</p>
    <p><a href="https://github.com/animint/animint2/issues/322">Source updates</a></p>
  `;
  body.append(footer);

  document.querySelector("[data-theme-toggle]")?.addEventListener("click", () => {
    applyTheme(root.dataset.theme === "dark" ? "light" : "dark");
  });

  const toggle = document.querySelector(".nav-toggle");
  const cluster = document.querySelector(".nav-cluster");
  toggle?.addEventListener("click", () => {
    const open = toggle.getAttribute("aria-expanded") === "true";
    toggle.setAttribute("aria-expanded", String(!open));
    cluster?.classList.toggle("is-open", !open);
  });

  const weekShell = document.querySelector("[data-week-nav]");
  if (weekShell) {
    weekShell.innerHTML = `
      <nav class="week-nav" aria-label="Weekly journal navigation">
        ${weekNav
          .map((item) => {
            const active = page === `journal-${item.id}` || (page === "journal" && item.id === "week-1");
            return `<a class="week-nav-link${active ? " is-active" : ""}" ${active ? 'aria-current="page"' : ""} href="${item.href}">${item.label}</a>`;
          })
          .join("")}
      </nav>
    `;
    const activeLink = weekShell.querySelector(".is-active");
    if (activeLink && window.matchMedia("(max-width: 767px)").matches) {
      activeLink.scrollIntoView({ block: "nearest", inline: "center" });
    }
  }

  const toc = document.querySelector("[data-page-toc]");
  if (toc) {
    const headings = [...document.querySelectorAll("main.content h2[id]")];
    if (headings.length) {
      toc.innerHTML = `
        <p class="toc-title">Index</p>
        <ul>
          ${headings
            .map((heading) => `<li><a href="#${heading.id}">${heading.textContent}</a></li>`)
            .join("")}
        </ul>
      `;
      const links = [...toc.querySelectorAll("a")];
      const sync = () => {
        const current = headings.findLast((heading) => heading.getBoundingClientRect().top <= 140) || headings[0];
        links.forEach((link) => {
          link.classList.toggle("active", link.getAttribute("href") === `#${current.id}`);
        });
      };
      sync();
      window.addEventListener("scroll", sync, { passive: true });
    }
  }
})();
