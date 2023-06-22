let userMenuBtn = document.querySelector('#userMenuBtn'),
	userMenuBtnArrow = document.querySelector('#userMenuBtnArrow'),
	userMenu = document.querySelector('#userMenu');

userMenuBtn.onclick = () => {
	userMenu.classList.toggle('hide-element');
	if (userMenu.classList.contains('hide-element')) {
		userMenuBtnArrow.innerHTML = '►';
	}
	else {
		userMenuBtnArrow.innerHTML = '▼';
	}
}