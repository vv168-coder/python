import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vite.dev/config/
export default defineConfig({
  plugins: [
    vue(),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },
  server: {// api/system/slider/list
    proxy: {
      '/api': {
        target: 'http://localhost:8000',
        changeOrigin: true,//是否跨域,支持跨域
        rewrite: path => path.replace(/^\/api/, '')
      }
    }
  }
})

