import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// Usa variável de ambiente BACKEND_URL, se não existir cai no localhost
const backendTarget = process.env.BACKEND_URL || 'http://localhost:8000'

export default defineConfig({
  plugins: [react()],
  server: {
    host: '0.0.0.0', // expõe para fora do container
    port: 3000,      // força a porta 3000
    proxy: {
      '/api': {
        target: backendTarget,
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api/, '')
      }
    }
  }
})
