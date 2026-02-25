<script setup lang="ts">
  import { computed } from 'vue';

  const props = withDefaults(defineProps<{
    image?: string
  }>(), {
    image: 'https://cover.sli.dev'
  })

  const imageURL = computed(() => {
    return new URL(props.image).href
  })  

</script>

<template>
  <div class="slidev-layout section">
    <div class="my-auto w-full">
      <slot />
      <div class="triangle-overlay">
        <img
          :src="props.image"
          alt="Section Image"
          style="position: absolute; bottom: 10%; right: 5%; width: 30%; height: auto; z-index: 2; object-fit: contain; opacity: 0.85;"
        />
      </div>
    </div>
  </div>
</template>

<style>
  .slidev-layout.section {
    background-color: var(--slidev-background);
    color: var(--slidev-primary);
  }
  .slidev-layout.section .triangle-overlay {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: var(--slidev-accent);
    clip-path: polygon(100% 100%, 100% -50%, 25% 100%);
    z-index: 1;
  }

  .slidev-layout.section h1 {
    color: var(--slidev-primary);
  }
  .slidev-layout.section h2 {
    color: var(--slidev-primary);
    opacity: .7;
  }
</style>

