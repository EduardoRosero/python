#
#
validator = GoogleIDToken::Validator.new
claim = validatos.check(params['id_token'], audience, audience)

if claim
	session[:user_id]=claim['sub']
	session[:user_email]=claim['email']
	redirect '/'
else
	logger.info('No valid identify token present')
end

#Cuando se ejecutan funciones lo mejor es utilizar parentesis

#Se recomienda utilizar variables con snakecase es decir separadas_por_guiones_bajos

#Se recomienda para las clases utilizar letra capital paraMuchasPalabras