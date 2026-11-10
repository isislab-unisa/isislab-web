
document.addEventListener('DOMContentLoaded', function () {

  const galleries = document.querySelectorAll(
    '.seminar-gallery, .getting-here-steps, .getting-here-map'
  );

  galleries.forEach(function (gallery) {

    gallery.querySelectorAll('a').forEach(function (link) {

      link.addEventListener('click', function (event) {

        const thumbnail = link.querySelector('img');

        if (!thumbnail || !link.href) return;

        event.preventDefault();

        const lightbox = document.createElement('div');
        lightbox.className = 'seminar-lightbox';
        lightbox.setAttribute('role', 'dialog');
        lightbox.setAttribute('aria-modal', 'true');
        lightbox.setAttribute('aria-label', 'Anteprima immagine');

        const image = document.createElement('img');
        image.src = link.href;
        image.alt = thumbnail.alt || '';

        const closeButton = document.createElement('button');
        closeButton.className = 'seminar-lightbox-close';
        closeButton.type = 'button';
        closeButton.innerHTML = '&times;';
        closeButton.setAttribute('aria-label', 'Chiudi immagine');

        lightbox.appendChild(image);
        lightbox.appendChild(closeButton);

        document.body.appendChild(lightbox);
        document.body.style.overflow = 'hidden';

        function closeLightbox() {
          lightbox.remove();
          document.body.style.overflow = '';
          document.removeEventListener('keydown', handleKeydown);
        }

        function handleKeydown(event) {
          if (event.key === 'Escape') {
            closeLightbox();
          }
        }

        closeButton.addEventListener('click', closeLightbox);

        lightbox.addEventListener('click', function (event) {
          if (event.target === lightbox) {
            closeLightbox();
          }
        });

        image.addEventListener('click', function (event) {
          event.stopPropagation();
        });

        document.addEventListener('keydown', handleKeydown);

        closeButton.focus();

      });

    });

  });

});
