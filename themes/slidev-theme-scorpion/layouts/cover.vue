<template>
  <div class="slidev-layout cover">
    <img src="../assets/scorpion.png" alt="Scorpion" style="position: absolute; top: -10%; right: -7%; width: 50%"/>
    <div class="my-auto w-full">
      <slot />
    </div>
  </div>
</template>

<style>
  .slidev-layout.cover {
    background-color: var(--slidev-footer-bg);
    color: var(--slidev-footer-text);
  }
</style>