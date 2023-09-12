/* cusom js file made by JenDoe */

const showHiddenpass = (loginPass, loginEye) =>{
	const input = document.getElementById(loginPass),
		  iconEye = document.getElementById(loginEye)
	iconEye.addEventListener('click', () =>{
		// Change password to text
		if(input.type === 'password'){
			//Switch to text
			input.type = 'text'
			// Icon change
			iconEye.classList.add('fa-eye')
			iconEye.classList.remove('fa-eye-slash')
		}else{
			// Change to password
			input.type = 'password'
			
			//Icon change
			iconEye.classList.remove('fa-eye')
			iconEye.classList.add('fa-eye-slash')
		}
	})
}

showHiddenpass('login-pass', 'login-eye')




















