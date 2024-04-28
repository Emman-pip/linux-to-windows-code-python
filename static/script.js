const timer = (id) => {
	const target = document.getElementById(id)
	fetch("/timer").then(res => res.text()).then((res) => {
		target.innerHTML = res
	}).then(() => console.log("success"))
}
