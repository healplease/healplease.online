<template>
  <v-container class="fill-height d-flew flex-column" max-width="900">
    <div class="align-self-start text-h3 ma-2">
      {{ headline }}
    </div>
    <div class-="mt-5">Software dev, and a lot of other things.</div>
    <v-spacer />
    <div class="align-self-end">
      <v-btn
        v-for="link in links"
        :key="link.url"
        :href="link.url"
        class="ma-2"
        target="_blank"
        rel="noopener"
        icon
      >
        <v-icon :icon="link.icon" size="36" />
      </v-btn>
    </div>
  </v-container>
</template>

<script lang="ts">

export default {
  data() {
    return {
      headline: 'healplease',
      links: [
        {
          icon: 'mdi-linkedin',
          url: 'https://www.linkedin.com/in/healplease',
        },
        {
          icon: 'mdi-github',
          url: 'https://github.com/healplease',
        },
        {
          icon: 'mdi-gmail',
          url: 'mailto:gavaalex2012@gmail.com',
        },
        {
          icon: 'mdi-instagram',
          url: 'https://www.instagram.com/kekus_lolus/',
        },
      ],
    };
  },
};
</script>
