require 'sinatra'

class NewApp < Sinatra::Base
	get '/cgi-bin/migrated-page.rb' do
		"This is a migrated sinatra page: #{params}"
	end
end
