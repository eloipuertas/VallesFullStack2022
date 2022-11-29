<!-- template for the disk model with title, artist and genre-->
<template>
  <div>
    <div class="disk">
      <div class="title"> {{ disk.title }}</div>
      <div class="artist"> {{ disk.artist }}</div>
      <div class="genre"> {{ disk.genre }}</div>
    </div>
  </div>
</template>

// Path: client/src/components/Disk.vue
<script>
export default {
  name: 'Disk-detail',
  props: {
    disk: Object,
  },
};
</script>

// Path: client/src/components/Disk.vue
<style scoped>
.disk {
  border: 1px solid black;
  padding: 1em;
  margin: 1em;
  width: 200px;
  height: 200px;
}
</style>


