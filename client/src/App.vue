<!-- create app vue for component DiskList-->
<template>
  <div id="app">
    <DiskList />
  </div>
</template>

<script>
import DiskList from './components/DiskList';

export default {
  name: 'App',
  components: {
    DiskList,
  },
};
</script>

<!-- Path: client/src/App.vue -->
<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>

<!-- Path: client/src/App.vue -->
