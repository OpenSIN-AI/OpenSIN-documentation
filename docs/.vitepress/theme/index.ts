import DefaultTheme from 'vitepress/theme'
import HomeChoosePath from './components/HomeChoosePath.vue'
import HomeRelatedTopics from './components/HomeRelatedTopics.vue'
import './custom.css'

export default {
  ...DefaultTheme,
  enhanceApp({ app }) {
    app.component('HomeChoosePath', HomeChoosePath)
    app.component('HomeRelatedTopics', HomeRelatedTopics)
  },
}
