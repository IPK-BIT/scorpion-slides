<script setup lang="ts">
    let masks = [
        [[25.25,28], [5,30]],
    ]

</script>

<template>
<div style="position: relative; width: 100%; aspect-ratio: 16 / 9; max-height: 40vh;">

  <img class="absolute top-0 left-[9%] w-[82%] h-[100%] bg-black" src="/assets/coords-2.png"/>
    <div v-for="(mask, idx) in masks" :key="idx">
        <div v-click="['+0','+1']">
            <div :style="{
              position: 'absolute',
              top: '0%',
              left: '9%',
              width: mask[0][0]+'%',
              height: '100%',
              backgroundColor: 'rgba(0,0,0,0.5)'
            }"/>
            <div :style="{
                position: 'absolute',
                top: '0%',
                left: 9+mask[0][0]+'%',
                width: (9-mask[0][0])+mask[1][1]+'%',
                height: mask[0][1]+'%',
                backgroundColor: 'rgba(0,0,0,0.5)'
            }"/>
            <!-- <div :style="{
                position: 'absolute',
                top: mask[0][1]+mask[1][0]+'%',
                left: 9+mask[0][0]+'%',
                width: 9+mask[1][1]+'%',
                height: 100-(mask[1][0]+mask[0][1])+'%',
                backgroundColor: 'rgba(0,0,0,0.5)'
            }"/>
            <div :style="{
                position: 'absolute',
                top: '0%',
                left: 9+mask[1][1]+'%',
                width: 9+mask[0][0]+'%',
                height: 100-(mask[0][1])+'%',
                backgroundColor: 'rgba(0,0,0,0.5)'
            }"/> -->
        </div>
    </div>
</div>
</template>