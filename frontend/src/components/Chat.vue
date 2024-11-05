<template>
  <a-card class="chat-container" title="Apollo Bot - Chat">
    <a-list
      class="chat-messages"
      :dataSource="messages"
      :renderItem="renderMessage"
      bordered
    />
    <a-space class="chat-input" direction="horizontal" style="width: 100%;" align="center">
      <a-input
        v-model="newMessage"
        placeholder="Digite sua mensagem..."
        @pressEnter="sendMessage"
      />
      <a-button type="primary" @click="sendMessage">Enviar</a-button>
    </a-space>
  </a-card>
</template>

<script>
import { ref } from 'vue'

export default {
  name: 'Chat',
  setup() {
    const messages = ref([]) // Estado das mensagens do chat
    const newMessage = ref('') // Estado da nova mensagem digitada

    const sendMessage = () => {
      if (newMessage.value.trim()) {
        messages.value.push({
          text: newMessage.value,
          sender: 'Usuário',
        })
        newMessage.value = ''
        // Aqui podemos também enviar a mensagem ao backend via WebSocket ou API
      }
    }

    const renderMessage = (message) => (
      <a-list-item>
        <a-typography-text
          :type="message.sender === 'Usuário' ? 'secondary' : 'success'"
        >
          <strong>{{ message.sender }}:</strong> {{ message.text }}
        </a-typography-text>
      </a-list-item>
    )

    return { messages, newMessage, sendMessage, renderMessage }
  },
}
</script>

<style scoped>
.chat-container {
  max-width: 400px;
  margin: 0 auto;
  padding: 10px;
  height: 80vh;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.chat-messages {
  flex: 1;
  overflow-y: auto;
  margin-bottom: 10px;
}

.chat-input {
  display: flex;
  gap: 10px;
}
</style>
