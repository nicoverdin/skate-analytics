import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import path from 'path'

export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'),
    },
  },
  server: {
    host: '0.0.0.0', // Imprescindible para Docker
    port: 5173,
    watch: {
      usePolling: true, // Útil si los cambios no se ven en Docker
    },
  },
})