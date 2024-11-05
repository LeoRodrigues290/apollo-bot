<template>
  <div class="min-h-screen flex bg-gray-100">
    <!-- Sidebar -->
    <Sidebar />

    <!-- Conteúdo Principal -->
    <main class="flex-1 flex items-center justify-center p-6">
      <Chat />
    </main>
  </div>
</template>

<script>
import Chat from './components/Chat.vue'
import Sidebar from './components/Sidebar.vue'

export default {
  name: 'App',
  components: {
    Chat,
    Sidebar,
  },
}
</script>

<style scoped>
</style>
