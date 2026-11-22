/**
 * FARAN SPORTS — Main JavaScript
 * Handles animations, UI interactions, carousel, search, filter, and WhatsApp order flow.
 */

(function () {
  'use strict';

  document.addEventListener('DOMContentLoaded', function () {
    initPreloader();
    initNavbar();
    initHeroAnimations();
    initScrollReveal();
    initCounters();
    initSearchOverlay();
    initTestimonialCarousel();
    initProductDetail();
    initProductFilters();
    initBackToTop();
  });

  /* -------------------------------------------------------------
     1. PRELOADER
     ------------------------------------------------------------- */
  function initPreloader() {
    const preloader = document.querySelector('.preloader');
    if (!preloader) return;

    window.addEventListener('load', function () {
      setTimeout(function () {
        preloader.classList.add('hidden');
      }, 350);
    });

    // Fallback if load already fired
    if (document.readyState === 'complete') {
      setTimeout(function () {
        preloader.classList.add('hidden');
      }, 300);
    }
  }

  /* -------------------------------------------------------------
     2. NAVBAR & MOBILE MENU
     ------------------------------------------------------------- */
  function initNavbar() {
    const navbar = document.querySelector('.navbar');
    const hamburger = document.querySelector('.hamburger');
    const mobileMenu = document.querySelector('.mobile-menu');

    // Sticky glassmorphism effect
    function handleScroll() {
      if (!navbar) return;
      if (window.scrollY > 40) {
        navbar.classList.add('scrolled');
      } else {
        navbar.classList.remove('scrolled');
      }
    }

    window.addEventListener('scroll', handleScroll, { passive: true });
    handleScroll();

    // Mobile menu toggle
    if (hamburger && mobileMenu) {
      hamburger.addEventListener('click', function () {
        const isOpen = hamburger.classList.toggle('active');
        mobileMenu.classList.toggle('open', isOpen);
        document.body.style.overflow = isOpen ? 'hidden' : '';
      });

      // Close menu when clicking navigation links
      const mobileLinks = mobileMenu.querySelectorAll('a');
      mobileLinks.forEach(function (link) {
        link.addEventListener('click', function () {
          hamburger.classList.remove('active');
          mobileMenu.classList.remove('open');
          document.body.style.overflow = '';
        });
      });
    }
  }

  /* -------------------------------------------------------------
     3. HERO ANIMATIONS
     ------------------------------------------------------------- */
  function initHeroAnimations() {
    const lines = document.querySelectorAll('.hero-title .line-inner');
    const subtitle = document.querySelector('.hero-subtitle');
    const buttons = document.querySelector('.hero-buttons');

    if (!lines.length && !subtitle) return;

    setTimeout(function () {
      lines.forEach(function (line) {
        line.classList.add('visible');
      });
      if (subtitle) subtitle.classList.add('visible');
      if (buttons) buttons.classList.add('visible');
    }, 200);
  }

  /* -------------------------------------------------------------
     4. SCROLL REVEAL (IntersectionObserver)
     ------------------------------------------------------------- */
  function initScrollReveal() {
    const reveals = document.querySelectorAll('.reveal');
    if (!reveals.length) return;

    if ('IntersectionObserver' in window) {
      const observer = new IntersectionObserver(
        function (entries) {
          entries.forEach(function (entry) {
            if (entry.isIntersecting) {
              entry.target.classList.add('visible');
              observer.unobserve(entry.target);
            }
          });
        },
        { threshold: 0.12, rootMargin: '0px 0px -40px 0px' }
      );

      reveals.forEach(function (el) {
        observer.observe(el);
      });
    } else {
      // Fallback
      reveals.forEach(function (el) {
        el.classList.add('visible');
      });
    }
  }

  /* -------------------------------------------------------------
     5. STAT & TRUST COUNTERS
     ------------------------------------------------------------- */
  function initCounters() {
    const counterElements = document.querySelectorAll('[data-counter]');
    if (!counterElements.length) return;

    function startCounting(el) {
      const target = parseFloat(el.getAttribute('data-counter'));
      const prefix = el.getAttribute('data-prefix') || '';
      const suffix = el.getAttribute('data-suffix') || '';
      const duration = 1600;
      const startTime = performance.now();

      function updateCounter(currentTime) {
        const elapsed = currentTime - startTime;
        const progress = Math.min(elapsed / duration, 1);
        // Ease out quad
        const easeOut = 1 - (1 - progress) * (1 - progress);
        const currentVal = Math.floor(easeOut * target);

        el.textContent = `${prefix}${currentVal.toLocaleString()}${suffix}`;

        if (progress < 1) {
          requestAnimationFrame(updateCounter);
        } else {
          el.textContent = `${prefix}${target.toLocaleString()}${suffix}`;
        }
      }

      requestAnimationFrame(updateCounter);
    }

    if ('IntersectionObserver' in window) {
      const observer = new IntersectionObserver(
        function (entries) {
          entries.forEach(function (entry) {
            if (entry.isIntersecting) {
              startCounting(entry.target);
              observer.unobserve(entry.target);
            }
          });
        },
        { threshold: 0.3 }
      );

      counterElements.forEach(function (el) {
        observer.observe(el);
      });
    } else {
      counterElements.forEach(startCounting);
    }
  }

  /* -------------------------------------------------------------
     6. SEARCH OVERLAY & LIVE SEARCH
     ------------------------------------------------------------- */
  function initSearchOverlay() {
    const searchOverlay = document.querySelector('.search-overlay');
    const searchTriggers = document.querySelectorAll('[data-open-search]');
    const searchClose = document.querySelector('.search-close');
    const searchInput = document.querySelector('.search-input-wrapper input');
    const searchResults = document.querySelector('.search-results');

    if (!searchOverlay) return;

    function openSearch() {
      searchOverlay.classList.add('open');
      document.body.style.overflow = 'hidden';
      if (searchInput) {
        setTimeout(function () {
          searchInput.focus();
        }, 150);
      }
    }

    function closeSearch() {
      searchOverlay.classList.remove('open');
      document.body.style.overflow = '';
      if (searchInput) searchInput.value = '';
      if (searchResults) searchResults.innerHTML = '';
    }

    searchTriggers.forEach(function (btn) {
      btn.addEventListener('click', function (e) {
        e.preventDefault();
        openSearch();
      });
    });

    if (searchClose) {
      searchClose.addEventListener('click', closeSearch);
    }

    // Close when clicking outside container
    searchOverlay.addEventListener('click', function (e) {
      if (e.target === searchOverlay) {
        closeSearch();
      }
    });

    // Close with Esc key
    window.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && searchOverlay.classList.contains('open')) {
        closeSearch();
      }
    });

    // Live search debounced
    if (searchInput && searchResults) {
      let debounceTimer;
      searchInput.addEventListener('input', function () {
        const query = this.value.trim().toLowerCase();
        clearTimeout(debounceTimer);

        if (!query) {
          searchResults.innerHTML = '';
          return;
        }

        debounceTimer = setTimeout(function () {
          fetch(`/api/products?query=${encodeURIComponent(query)}`)
            .then(function (res) {
              return res.json();
            })
            .then(function (data) {
              const matches = (data.products || []).filter(function (p) {
                return (
                  p.name.toLowerCase().includes(query) ||
                  p.category.toLowerCase().includes(query) ||
                  p.brand.toLowerCase().includes(query) ||
                  (p.description && p.description.toLowerCase().includes(query))
                );
              });

              if (matches.length === 0) {
                searchResults.innerHTML = `
                  <div style="padding: 24px; text-align: center; color: var(--text-muted);">
                    No sports gear found matching "${escapeHtml(query)}"
                  </div>`;
                return;
              }

              searchResults.innerHTML = matches
                .slice(0, 6)
                .map(function (p) {
                  return `
                  <a href="/product/${p.id}" class="search-result-item">
                    <div class="search-result-thumb">
                      <div class="sport-thumb-icon">${getCategoryEmoji(p.category)}</div>
                    </div>
                    <div>
                      <div class="search-result-name">${escapeHtml(p.name)}</div>
                      <div class="search-result-category">${escapeHtml(p.brand.toUpperCase())} • ₹${p.price.toLocaleString()}</div>
                    </div>
                  </a>`;
                })
                .join('');
            })
            .catch(function (err) {
              console.error('Search error:', err);
            });
        }, 220);
      });
    }
  }

  function getCategoryEmoji(cat) {
    const map = {
      cricket: '🏏',
      badminton: '🏸',
      football: '⚽',
      'gym-equipment': '🏋️',
      'fitness-supplements': '💊',
      running: '🏃',
      'table-tennis': '🏓'
    };
    return map[cat] || '🏆';
  }

  function escapeHtml(str) {
    return str
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#039;');
  }

  /* -------------------------------------------------------------
     7. TESTIMONIALS CAROUSEL
     ------------------------------------------------------------- */
  function initTestimonialCarousel() {
    const carousel = document.querySelector('.testimonials-carousel');
    if (!carousel) return;

    const track = carousel.querySelector('.testimonials-track');
    const cards = carousel.querySelectorAll('.testimonial-card');
    const prevBtn = document.querySelector('.carousel-btn.prev');
    const nextBtn = document.querySelector('.carousel-btn.next');
    const dotsContainer = document.querySelector('.carousel-dots');

    if (!track || !cards.length) return;

    let currentIndex = 0;
    let cardsPerView = getCardsPerView();
    let maxIndex = Math.max(0, cards.length - cardsPerView);

    function getCardsPerView() {
      if (window.innerWidth >= 1024) return 3;
      if (window.innerWidth >= 768) return 2;
      return 1;
    }

    function createDots() {
      if (!dotsContainer) return;
      dotsContainer.innerHTML = '';
      const dotCount = maxIndex + 1;
      for (let i = 0; i < dotCount; i++) {
        const dot = document.createElement('div');
        dot.className = `carousel-dot ${i === currentIndex ? 'active' : ''}`;
        dot.addEventListener('click', function () {
          goToSlide(i);
        });
        dotsContainer.appendChild(dot);
      }
    }

    function updateDots() {
      if (!dotsContainer) return;
      const dots = dotsContainer.querySelectorAll('.carousel-dot');
      dots.forEach(function (dot, i) {
        dot.classList.toggle('active', i === currentIndex);
      });
    }

    function updateTrack() {
      const percentage = (100 / cardsPerView) * currentIndex;
      track.style.transform = `translateX(-${percentage}%)`;
      updateDots();
    }

    function goToSlide(index) {
      currentIndex = Math.max(0, Math.min(index, maxIndex));
      updateTrack();
    }

    if (prevBtn) {
      prevBtn.addEventListener('click', function () {
        if (currentIndex > 0) {
          goToSlide(currentIndex - 1);
        } else {
          goToSlide(maxIndex); // Loop
        }
      });
    }

    if (nextBtn) {
      nextBtn.addEventListener('click', function () {
        if (currentIndex < maxIndex) {
          goToSlide(currentIndex + 1);
        } else {
          goToSlide(0); // Loop
        }
      });
    }

    window.addEventListener(
      'resize',
      debounce(function () {
        cardsPerView = getCardsPerView();
        maxIndex = Math.max(0, cards.length - cardsPerView);
        createDots();
        goToSlide(Math.min(currentIndex, maxIndex));
      }, 150)
    );

    createDots();
    updateTrack();

    // Auto-advance every 6 seconds
    let autoSlideTimer = setInterval(function () {
      if (currentIndex < maxIndex) {
        goToSlide(currentIndex + 1);
      } else {
        goToSlide(0);
      }
    }, 6000);

    carousel.addEventListener('mouseenter', function () {
      clearInterval(autoSlideTimer);
    });
    carousel.addEventListener('mouseleave', function () {
      autoSlideTimer = setInterval(function () {
        if (currentIndex < maxIndex) {
          goToSlide(currentIndex + 1);
        } else {
          goToSlide(0);
        }
      }, 6000);
    });
  }

  /* -------------------------------------------------------------
     8. PRODUCT DETAIL INTERACTIONS
     ------------------------------------------------------------- */
  function initProductDetail() {
    // Gallery thumbnails
    const mainImg = document.querySelector('.gallery-main img');
    const mainPlaceholder = document.querySelector('.gallery-main .sport-badge-visual');
    const thumbs = document.querySelectorAll('.gallery-thumb');

    thumbs.forEach(function (thumb) {
      thumb.addEventListener('click', function () {
        thumbs.forEach(function (t) {
          t.classList.remove('active');
        });
        thumb.classList.add('active');
        const newSrc = thumb.getAttribute('data-img');
        if (newSrc && mainImg) {
          mainImg.src = newSrc;
        }
      });
    });

    // Size selector
    const sizeOptions = document.querySelectorAll('.size-option');
    sizeOptions.forEach(function (option) {
      option.addEventListener('click', function () {
        sizeOptions.forEach(function (opt) {
          opt.classList.remove('selected');
        });
        option.classList.add('selected');

        // Dynamically update WhatsApp button message with selected size
        const selectedSize = option.getAttribute('data-size');
        const waBtn = document.querySelector('.btn-order-whatsapp-large');
        if (waBtn && selectedSize) {
          const originalUrl = waBtn.getAttribute('data-base-url') || waBtn.href;
          if (!waBtn.getAttribute('data-base-url')) {
            waBtn.setAttribute('data-base-url', originalUrl);
          }
          const updatedMsg = originalUrl + encodeURIComponent(`\nSelected Size/Variant: ${selectedSize}`);
          waBtn.href = updatedMsg;
        }
      });
    });
  }

  /* -------------------------------------------------------------
     9. PRODUCT FILTERING & VIEW TOGGLE
     ------------------------------------------------------------- */
  function initProductFilters() {
    const productsGrid = document.querySelector('.products-grid');
    const viewButtons = document.querySelectorAll('.view-toggle button');
    const sortSelect = document.querySelector('.sort-dropdown select');
    const filterChecks = document.querySelectorAll('.filter-check input');

    // View toggle (Grid / List)
    if (viewButtons.length && productsGrid) {
      viewButtons.forEach(function (btn) {
        btn.addEventListener('click', function () {
          viewButtons.forEach(function (b) {
            b.classList.remove('active');
          });
          btn.classList.add('active');
          const view = btn.getAttribute('data-view');
          if (view === 'list') {
            productsGrid.classList.add('list-view');
          } else {
            productsGrid.classList.remove('list-view');
          }
        });
      });
    }

    // Sort select change
    if (sortSelect) {
      sortSelect.addEventListener('change', function () {
        applyFilters();
      });
    }

    // Checkbox filter changes
    filterChecks.forEach(function (chk) {
      chk.addEventListener('change', function () {
        applyFilters();
      });
    });

    function applyFilters() {
      const selectedCategories = Array.from(
        document.querySelectorAll('input[name="category"]:checked')
      ).map(function (el) {
        return el.value;
      });

      const selectedBrands = Array.from(
        document.querySelectorAll('input[name="brand"]:checked')
      ).map(function (el) {
        return el.value;
      });

      const sortVal = sortSelect ? sortSelect.value : '';

      // If on standard products page, update URL query or fetch via API
      const params = new URLSearchParams();
      if (selectedCategories.length === 1) {
        params.set('category', selectedCategories[0]);
      }
      if (selectedBrands.length === 1) {
        params.set('brand', selectedBrands[0]);
      }
      if (sortVal) {
        params.set('sort', sortVal);
      }

      // Smooth client-side filter if cards are present
      const cards = document.querySelectorAll('.products-grid .product-card');
      let visibleCount = 0;

      cards.forEach(function (card) {
        const cardCategory = card.getAttribute('data-category');
        const cardBrand = card.getAttribute('data-brand');
        const matchCat =
          selectedCategories.length === 0 || selectedCategories.includes(cardCategory);
        const matchBrand =
          selectedBrands.length === 0 || selectedBrands.includes(cardBrand);

        if (matchCat && matchBrand) {
          card.style.display = '';
          visibleCount++;
        } else {
          card.style.display = 'none';
        }
      });

      const resultsCountEl = document.querySelector('.results-count span');
      if (resultsCountEl) {
        resultsCountEl.textContent = visibleCount;
      }
    }
  }

  /* -------------------------------------------------------------
     10. BACK TO TOP BUTTON
     ------------------------------------------------------------- */
  function initBackToTop() {
    const backBtn = document.querySelector('.back-to-top');
    if (!backBtn) return;

    window.addEventListener(
      'scroll',
      function () {
        if (window.scrollY > 450) {
          backBtn.classList.add('visible');
        } else {
          backBtn.classList.remove('visible');
        }
      },
      { passive: true }
    );

    backBtn.addEventListener('click', function () {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  /* -------------------------------------------------------------
     HELPERS
     ------------------------------------------------------------- */
  function debounce(func, wait) {
    let timeout;
    return function () {
      const context = this;
      const args = arguments;
      clearTimeout(timeout);
      timeout = setTimeout(function () {
        func.apply(context, args);
      }, wait);
    };
  }
})();
