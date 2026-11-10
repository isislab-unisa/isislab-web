
(() => {
  "use strict";

  function initProjectsFilter() {
    const searchInput = document.getElementById("project-search");
    const statusSelect = document.getElementById("project-status");
    const programSelect = document.getElementById("project-program");
    const typeSelect = document.getElementById("project-type");
    const yearSelect = document.getElementById("project-year");

    const clearButton = document.getElementById("projects-clear");
    const countElement = document.getElementById("projects-count");
    const noResults = document.getElementById("projects-no-results");

    const cards = Array.from(document.querySelectorAll(".project-card"));
    const groups = Array.from(document.querySelectorAll(".project-year-group"));

    if (!searchInput || !statusSelect || !programSelect ||
        !typeSelect || !yearSelect || !clearButton || !countElement) {
      console.error("Projects filter: elementi HTML mancanti.");
      return;
    }

    if (cards.length === 0) {
      console.warn("Projects filter: nessuna scheda progetto trovata.");
      return;
    }

    const singular = countElement.dataset.singular || "progetto";
    const plural = countElement.dataset.plural || "progetti";

    function normalize(value) {
      return (value || "")
        .toString()
        .trim()
        .toLocaleLowerCase();
    }

    function applyFilters() {
      const query = normalize(searchInput.value);
      const selectedStatus = statusSelect.value;
      const selectedProgram = programSelect.value;
      const selectedType = typeSelect.value;
      const selectedYear = yearSelect.value;

      let visibleCount = 0;

      cards.forEach((card) => {
        const cardStatus = card.dataset.status || "";
        const cardProgram = card.dataset.program || "";
        const cardTypes = (card.dataset.types || "")
          .split("|")
          .filter(Boolean);
        const cardYear = card.dataset.year || "";
        const cardText = normalize(card.dataset.search);

        const matchesSearch = !query || cardText.includes(query);
        const matchesStatus =
          selectedStatus === "all" || selectedStatus === cardStatus;
        const matchesProgram =
          selectedProgram === "all" || selectedProgram === cardProgram;
        const matchesType =
          selectedType === "all" || cardTypes.includes(selectedType);
        const matchesYear =
          selectedYear === "all" || selectedYear === cardYear;

        const visible =
          matchesSearch &&
          matchesStatus &&
          matchesProgram &&
          matchesType &&
          matchesYear;

        card.hidden = !visible;

        if (visible) visibleCount++;
      });

      groups.forEach((group) => {
        const visibleCards = group.querySelectorAll(
          ".project-card:not([hidden])"
        );
        group.hidden = visibleCards.length === 0;
      });

      countElement.textContent =
        `${visibleCount} ${visibleCount === 1 ? singular : plural}`;

      if (noResults) {
        noResults.hidden = visibleCount > 0;
      }
    }

    searchInput.addEventListener("input", applyFilters);
    statusSelect.addEventListener("change", applyFilters);
    programSelect.addEventListener("change", applyFilters);
    typeSelect.addEventListener("change", applyFilters);
    yearSelect.addEventListener("change", applyFilters);

    clearButton.addEventListener("click", () => {
      searchInput.value = "";
      statusSelect.value = "all";
      programSelect.value = "all";
      typeSelect.value = "all";
      yearSelect.value = "all";

      applyFilters();
    });

    applyFilters();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initProjectsFilter);
  } else {
    initProjectsFilter();
  }
})();
