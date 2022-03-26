async function fetchGasMex(url, method, expectedStatusCode = 200){
	let options = {
		headers: {
			"X-CSRFToken": getCookie('csrftoken')
		},
		method: method,
	};

	let response = await fetch(url, options);

	if(!response.ok || response.status != expectedStatusCode){
		message = `An error has occured, ${response.status} status code`;
		response = await response.json();
		let errors = {
				"message": message,
		}
		for(let error in response){
				errors[error] = response[error]
		}
		throw errors
	}else{
		response = await response.json();
		return response
	}
}

function getCookie(cname) {
	let name = cname + "=";
	let decodedCookie = decodeURIComponent(document.cookie);
	let ca = decodedCookie.split(';');
	for (let i = 0; i < ca.length; i++) {
		let c = ca[i];
		while (c.charAt(0) == ' ') {
			c = c.substring(1);
		}
		if (c.indexOf(name) == 0) {
			return c.substring(name.length, c.length);
		}
	}
	return "";
}
