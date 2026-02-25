<script setup>
import { useSlideContext } from '@slidev/client'
const { $slidev } = useSlideContext()
</script>

<template>
    <footer v-if="!['cover', 'section'].includes($slidev.nav.currentLayout)" style="bottom: 0; left: 0; position: absolute">
        <div class="flex flew-row justify-between items-center">
            <span style="display: flex; flex-direction: row; gap: .5rem; align-items: center;">
                <img src="../assets/scorpion.png" alt="Logo" style="height: 1rem; vertical-align: middle">
                <a target="_blank" href="https://scorpion.bi.denbi.de">Scorpion</a>
            </span>            
            <span>
                {{ $slidev.configs.title }}
            </span>
            <span>
                {{ String($slidev.nav.currentPage).padStart(2, '0') }} / {{ String($slidev.nav.total).padStart(2, '0') }}
            </span>
        </div>
    </footer>
</template>

<style>
    footer {
        width: 100%;
        padding: 0.25rem;
        background-color: var(--slidev-footer-bg, var(--slidev-bg));
        color: var(--slidev-footer-text, var(--slidev-text));
        font-size: 0.5rem;
        text-align: center;
    }
</style>