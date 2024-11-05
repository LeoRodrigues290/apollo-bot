<template>
  <div class="w-full max-w-lg mx-auto bg-white rounded-lg shadow-lg overflow-hidden flex flex-col h-[90vh]">
    <header class="bg-blue-600 text-white text-center py-4 font-semibold text-xl flex items-center justify-center space-x-2">
      <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" /></svg>
      <span>Suporte Apollo</span>
    </header>
    <div class="flex-1 p-4 overflow-y-auto space-y-4">
      <transition-group name="fade" tag="div">
        <div
          v-for="(message, index) in messages"
          :key="index"
          :class="message.sender === 'Usuário' ? 'text-right' : 'text-left'"
        >
          <div
            :class="{
              'bg-blue-100 text-blue-800 self-end': message.sender === 'Usuário',
              'bg-gray-100 text-gray-800 self-start': message.sender === 'Bot'
            }"
            class="inline-block px-4 py-2 rounded-lg max-w-xs"
          >
            <span class="font-medium">{{ message.sender }}:</span> {{ message.text }}
          </div>
        </div>
      </transition-group>
    </div>
    <div class="p-4 border-t flex items-center space-x-2">
      <input
        type="text"
        v-model="newMessage"
        placeholder="Digite sua mensagem..."
        @keyup.enter="sendMessage"
        class="flex-1 p-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
      />
      <button
        @click="sendMessage"
        class="px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700"
      >
        Enviar
      </button>
    </div>
  </div>
</template>

<script>
import { ref, onBeforeUnmount } from 'vue'
import { io } from 'socket.io-client'

export default {
  name: 'Chat',
  setup() {
    const messages = ref([]) // Estado das mensagens do chat
    const newMessage = ref('') // Estado da nova mensagem digitada

    // Conectar ao backend usando Socket.io
    const socket = io('http://localhost:5000') // URL do backend

    // Receber mensagens do backend
    socket.on('receive_message', (data) => {
      messages.value.push({
        text: data.text,
        sender: data.sender,
      })
    })

    const sendMessage = () => {
      if (newMessage.value.trim()) {
        // Adiciona a mensagem do usuário ao chat
        messages.value.push({
          text: newMessage.value,
          sender: 'Usuário',
        })

        // Envia a mensagem ao backend
        socket.emit('send_message', { message: newMessage.value })

        newMessage.value = '' // Limpa o campo de entrada
      }
    }

    // Desconectar ao sair do componente
    onBeforeUnmount(() => {
      socket.disconnect()
    })

    return { messages, newMessage, sendMessage }
  },
}
</script>

<style scoped>
  .fade-enter-active, .fade-leave-active {
    transition: opacity 0.5s;
  }
  .fade-enter, .fade-leave-to {
    opacity: 0;
  }
</style>
