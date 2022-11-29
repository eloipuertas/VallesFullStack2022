<template>
  <div v-if="disks">
    <h1>Disks in my library</h1>
    <Disk
        v-for="disk in disks"
        :key="disk._id"
        :disk="disk"
      />
  </div>
</template>
<script>
import Disk from './Disk.vue';
export default {
  name: 'Disk-list',
  components: {
    Disk,
  },
  data() {
    return {
      disks: null,
    };
  },
  async created() {
    const response = await fetch('https://eloipuertas-reimagined-space-waffle-54gqrjqjxg34p5r-5000.preview.app.github.dev/disks/'
      );
    this.disks = await response.json();
  },
};
</script>

// Path: client/src/components/DiskList.vue
<style scoped>
.disk-list {
  display: flex;
  flex-wrap: wrap;
}
</style>

