import DefaultTheme from 'vitepress/theme'
import CardIcon from './components/CardIcon.vue'
import OpenAIHome from './components/OpenAIHome.vue'
import OpenAIDocs from './components/OpenAIDocs.vue'
import OpenAILayout from './components/OpenAILayout.vue'
import './style.css'
import './custom.css'

// style.css carries the shared GitHub/Primer token baseline.
// custom.css layers OpenSIN-specific component overrides on top of that contract.
export default {
  ...DefaultTheme,
  Layout: OpenAILayout,
  enhanceApp({ app }) {
    app.component('CardIcon', CardIcon)
    app.component('OpenAIHome', OpenAIHome)
    app.component('OpenAIDocs', OpenAIDocs)
  },
}
