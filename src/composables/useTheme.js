import { ref, watch, onMounted } from 'vue'

const theme = ref('dark')

export function useTheme() {
  const toggleTheme = () => {
    theme.value = theme.value === 'dark' ? 'light' : 'dark'
    applyTheme(theme.value)
  }

  const applyTheme = (newTheme) => {
    document.body.classList.remove('light-theme', 'dark-theme')
    document.body.classList.add(newTheme + '-theme')
    localStorage.setItem('theme', newTheme)
  }

  onMounted(() => {
    const savedTheme = localStorage.getItem('theme') || 'dark'
    theme.value = savedTheme
    applyTheme(savedTheme)
  })

  watch(theme, (newTheme) => {
    applyTheme(newTheme)
  })

  return {
    theme,
    toggleTheme,
    applyTheme
  }
}
