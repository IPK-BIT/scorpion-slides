<script setup>
import { computed, ref } from 'vue'
import decks from './decks'

const searchTerm = ref('')
const selectedAuthor = ref('all')
const dateFrom = ref('')
const dateTo = ref('')

const authors = computed(() => {
  return [...new Set(decks.map((deck) => deck.author).filter(Boolean))].sort()
})

const filteredDecks = computed(() => {
  const term = searchTerm.value.trim().toLowerCase()

  return decks.filter((deck) => {
    const searchable = `${deck.title} ${deck.author} ${deck.id}`.toLowerCase()
    const matchesTerm = !term || searchable.includes(term)
    const matchesAuthor = selectedAuthor.value === 'all' || deck.author === selectedAuthor.value
    const matchesFrom = !dateFrom.value || (deck.date && deck.date >= dateFrom.value)
    const matchesTo = !dateTo.value || (deck.date && deck.date <= dateTo.value)

    return matchesTerm && matchesAuthor && matchesFrom && matchesTo
  })
})

const hasActiveFilters = computed(() => {
  return (
    searchTerm.value.trim() !== '' ||
    selectedAuthor.value !== 'all' ||
    dateFrom.value !== '' ||
    dateTo.value !== ''
  )
})

function resetFilters() {
  searchTerm.value = ''
  selectedAuthor.value = 'all'
  dateFrom.value = ''
  dateTo.value = ''
}

function formatDate(value) {
  if (!value) return 'Unknown date'

  const date = new Date(`${value}T00:00:00`)
  if (Number.isNaN(date.getTime())) return value

  return new Intl.DateTimeFormat(undefined, { dateStyle: 'medium' }).format(date)
}
</script>

<template>
  <main class="container">
    <header class="header">
      <h1>Slide Deck Gallery</h1>
      <p class="result-count">Showing {{ filteredDecks.length }} of {{ decks.length }} decks</p>
    </header>

    <div class="content-layout">
      <aside class="filters-sidebar" aria-label="Deck filters">
        <section class="facets">
          <div class="facet">
            <label for="filter-name">Name</label>
            <input
              id="filter-name"
              v-model="searchTerm"
              type="search"
              placeholder="Search title, author, or id"
            >
          </div>

          <div class="facet">
            <label for="filter-author">Author</label>
            <select id="filter-author" v-model="selectedAuthor">
              <option value="all">All authors</option>
              <option v-for="author in authors" :key="author" :value="author">{{ author }}</option>
            </select>
          </div>

          <div class="facet date-range">
            <label for="filter-from">Date range</label>
            <div class="date-inputs">
              <input id="filter-from" v-model="dateFrom" type="date">
              <input id="filter-to" v-model="dateTo" type="date">
            </div>
          </div>

          <div class="facet actions">
            <button type="button" class="reset" :disabled="!hasActiveFilters" @click="resetFilters">
              Reset filters
            </button>
          </div>
        </section>
      </aside>

      <section class="results-area">
        <div v-if="filteredDecks.length" class="grid">
          <a
            v-for="deck in filteredDecks"
            :key="deck.id"
            :href="deck.url"
            class="card"
            target="_blank"
            rel="noopener noreferrer"
          >
            <div class="card-body">
              <h2>{{ deck.title }}</h2>
              <p>{{ deck.description || 'No description available.' }}</p>
            </div>

            <div class="meta">
              <span>{{ deck.author }}</span>
              <span>{{ formatDate(deck.date) }}</span>
            </div>
          </a>
        </div>

        <section v-else class="empty-state" aria-live="polite">
          <h2>No decks match these filters</h2>
          <p>Try broadening your name query, choosing a different author, or widening the date range.</p>
          <button type="button" class="reset" @click="resetFilters">Clear all filters</button>
        </section>
      </section>
    </div>

    <div class="footer">
      <h2>Source Repositories</h2>
      <ul>
        <li>
          Scorpion-slides:
          <a href="https://github.com/ipk-bit/scorpion-slides">https://github.com/ipk-bit/scorpion-slides</a>
        </li>
        <li>
          These slide-decks present the Scorpion KPI Dashboard:
          <a href="https://github.com/scorpion-monitoring/scorpion">https://github.com/scorpion-monitoring/scorpion</a>
        </li>
      </ul>
    </div>
  </main>
</template>

<style>
.container {
  --app-text: var(--color-base-content);
  --app-muted: color-mix(in oklch, var(--color-base-content) 68%, var(--color-base-100));
  --panel-bg: color-mix(in oklch, var(--color-base-200) 82%, var(--color-base-100));
  --panel-border: color-mix(in oklch, var(--color-base-content) 10%, var(--color-base-100));
  --field-bg: color-mix(in oklch, var(--color-base-100) 90%, var(--color-base-200));
  --card-bg-start: var(--color-base-100);
  --card-bg-mid: color-mix(in oklch, var(--color-secondary) 26%, var(--color-base-100));
  --card-bg-end: color-mix(in oklch, var(--color-primary) 38%, var(--color-base-100));
  --card-border: color-mix(in oklch, var(--color-base-content) 18%, var(--color-base-100));
  --card-shadow: 0 10px 30px rgba(0, 0, 0, 0.08);
  --card-shadow-hover: 0 20px 50px rgba(0, 0, 0, 0.15);
  --meta-border: color-mix(in oklch, var(--color-base-content) 14%, var(--color-base-100));

  max-width: 1400px;
  margin: auto;
  min-height: 100dvh;
  padding: 3rem 2rem;
  display: flex;
  flex-direction: column;
  font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
    "Helvetica Neue", Arial, sans-serif;
  color: var(--app-text);
}

.header {
  margin-bottom: 1.5rem;
}

.header h1 {
  font-size: 2.4rem;
  margin: 0;
}

.subtitle {
  color: var(--app-muted);
  margin-top: 0.4rem;
  margin-bottom: 0;
}

.result-count {
  margin-top: 0.75rem;
  color: var(--app-muted);
  font-size: 0.95rem;
}

.content-layout {
  display: grid;
  grid-template-columns: 1fr;
  gap: 1.4rem;
  align-items: start;
  flex: 1;
}

.filters-sidebar {
  min-width: 0;
}

.results-area {
  min-width: 0;
}

.facets {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  padding: 1.1rem;
  border-radius: 14px;
  border: 1px solid var(--panel-border);
  background: var(--panel-bg);
}

.facet {
  display: flex;
  flex-direction: column;
  gap: 0.45rem;
}

.facet label,
.facet-title {
  font-size: 0.82rem;
  letter-spacing: 0.03em;
  text-transform: uppercase;
  color: var(--app-muted);
}

.facet input,
.facet select {
  border: 1px solid var(--panel-border);
  background: var(--field-bg);
  color: var(--app-text);
  border-radius: 10px;
  padding: 0.6rem 0.75rem;
  font: inherit;
}

.facet input:focus,
.facet select:focus,
.reset:focus {
  outline: 2px solid color-mix(in oklch, var(--color-primary) 70%, white);
  outline-offset: 2px;
}

.date-inputs {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  align-items: center;
}

.date-inputs input {
  width: 90%;
}

.actions {
  justify-content: flex-start;
}

.reset {
  border: 1px solid var(--panel-border);
  border-radius: 10px;
  background: color-mix(in oklch, var(--color-neutral) 60%, var(--field-bg));
  color: var(--app-text);
  padding: 0.58rem 0.9rem;
  font: inherit;
  cursor: pointer;
}

.reset:disabled {
  cursor: not-allowed;
  opacity: 0.55;
}

.grid {
  display: grid;
  gap: 1.8rem;
  grid-template-columns: 1fr;
}

@media (min-width: 640px) {
  .grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (min-width: 1024px) {
  .grid {
    grid-template-columns: repeat(3, 1fr);
  }
}

@media (min-width: 1400px) {
  .grid {
    grid-template-columns: repeat(4, 1fr);
  }
}

.card {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  text-decoration: none;
  color: inherit;
  background: linear-gradient(
    165deg,
    var(--card-bg-start) 0%,
    var(--card-bg-mid) 52%,
    var(--card-bg-end) 100%
  );
  border: 1px solid var(--card-border);
  border-radius: 16px;
  padding: 1.6rem 1.6rem 1.2rem;
  box-shadow: var(--card-shadow);
  transition: transform 0.2s ease, box-shadow 0.2s ease;
  min-height: 210px;
}

.card:hover {
  transform: translateY(-6px);
  box-shadow: var(--card-shadow-hover);
}

.card h2 {
  font-size: 1.2rem;
  margin: 0 0 0.4rem;
  line-height: 1.3;
}

.card p {
  font-size: 0.95rem;
  color: var(--app-muted);
  line-height: 1.4;
}

.meta {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 1.2rem;
  font-size: 0.8rem;
  color: var(--app-muted);
  border-top: 1px solid var(--meta-border);
  padding-top: 0.8rem;
}

.empty-state {
  margin: 1.5rem 0 2rem;
  padding: 1.5rem;
  border-radius: 14px;
  border: 1px dashed var(--panel-border);
  background: var(--panel-bg);
  text-align: left;
}

.empty-state h2 {
  margin: 0 0 0.4rem;
}

.empty-state p {
  margin: 0 0 1rem;
  color: var(--app-muted);
}

.footer {
  margin-top: 2rem;
  padding-top: 1rem;
  border-top: 1px solid color-mix(in oklch, var(--panel-border) 80%, transparent);
  text-align: left;
  color: var(--app-muted);
  font-size: 0.88rem;
  opacity: 0.9;
}

.footer h2 {
  margin: 0 0 0.6rem;
  font-size: 0.95rem;
  font-weight: 600;
  color: color-mix(in oklch, var(--app-text) 75%, var(--app-muted));
}

.footer ul {
  margin: 0;
  padding-left: 1rem;
}

.footer li + li {
  margin-top: 0.35rem;
}

.footer a {
  color: color-mix(in oklch, var(--color-primary) 45%, var(--app-muted));
}

.footer a:hover {
  color: color-mix(in oklch, var(--color-primary) 60%, var(--app-text));
}

@media (min-width: 1100px) {
  .content-layout {
    grid-template-columns: 300px minmax(0, 1fr);
    gap: 1.8rem;
  }

  .filters-sidebar {
    position: sticky;
    top: 1.25rem;
  }
}
</style>
