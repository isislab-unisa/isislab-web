
document.addEventListener("DOMContentLoaded", function () {
  const select = document.getElementById("project-program");
  const trigger = document.getElementById("project-program-button");
  const menu = document.getElementById("project-program-options");
  const current = document.querySelector(".project-program-current");

  if (!select || !trigger || !menu || !current) return;

  const options = menu.querySelectorAll(".project-program-option");

  function closeMenu() {
    menu.hidden = true;
    trigger.setAttribute("aria-expanded", "false");
  }

  function updateSelection(value) {
    const matchingOption = Array.from(select.options)
      .find(item => item.value === value);

    if (!matchingOption) return;

    current.textContent = matchingOption.textContent.trim();

    options.forEach(function (option) {
      const selected = option.dataset.value === value;
      option.classList.toggle("selected", selected);
      option.setAttribute("aria-selected", String(selected));
    });
  }

  trigger.addEventListener("click", function () {
    menu.hidden = !menu.hidden;
    trigger.setAttribute("aria-expanded", String(!menu.hidden));
  });

  options.forEach(function (option) {
    option.addEventListener("click", function () {
      const value = option.dataset.value;

      select.value = value;
      updateSelection(value);

      select.dispatchEvent(new Event("change", { bubbles: true }));
      closeMenu();
    });
  });

  select.addEventListener("change", function () {
    updateSelection(select.value);
  });

  document.addEventListener("click", function (event) {
    if (!event.target.closest(".project-program-dropdown")) {
      closeMenu();
    }
  });

  trigger.addEventListener("keydown", function (event) {
    if (event.key === "Escape") closeMenu();
  });

  updateSelection(select.value);
});
