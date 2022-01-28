function toggle_menu(id) {
  const element = document.querySelector(`#${id}`)

  if (element.classList.contains('opacity-0')) {
    element.classList.add('opacity-100', 'scale-100')
    element.classList.remove('opacity-0', 'scale-0')
  } else {
    element.classList.add('opacity-0', 'scale-0')
    element.classList.remove('opacity-100', 'scale-100')
  }
}