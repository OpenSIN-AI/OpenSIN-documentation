import DefaultTheme from 'vitepress/theme'
import HomeChoosePath from './components/HomeChoosePath.vue'
import HomeRelatedTopics from './components/HomeRelatedTopics.vue'
import ResourceCard from './components/ResourceCard.vue'
import OpenAIHome from './components/OpenAIHome.vue'
import OpenAIDocs from './components/OpenAIDocs.vue'
import OpenAILayout from './components/OpenAILayout.vue'
import './custom.css'

export default {
  ...DefaultTheme,
  Layout: OpenAILayout,
  enhanceApp({ app }) {
    app.component('HomeChoosePath', HomeChoosePath)
    app.component('HomeRelatedTopics', HomeRelatedTopics)
    app.component('ResourceCard', ResourceCard)
    app.component('OpenAIHome', OpenAIHome)
    app.component('OpenAIDocs', OpenAIDocs)
  },
}
