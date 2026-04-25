import DefaultTheme from 'vitepress/theme'
import CardIcon from './components/CardIcon.vue'
import OpenAIHome from './components/OpenAIHome.vue'
import OpenAIDocs from './components/OpenAIDocs.vue'
import OpenAILayout from './components/OpenAILayout.vue'
import './custom.css'

// Canonical docs baseline is defined in custom.css and the OpenAI-inspired layout components.
export default {
  ...DefaultTheme,
  Layout: OpenAILayout,
  enhanceApp({ app }) {
    app.component('CardIcon', CardIcon)
    app.component('OpenAIHome', OpenAIHome)
    app.component('OpenAIDocs', OpenAIDocs)
  },
}
