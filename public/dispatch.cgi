#!/home/besen/.rvm/wrappers/ruby-2.3.3/ruby

require 'rubygems'
require 'bundler/setup'
require "rack"

class Dispatcher
	def call(env)
		if env["SCRIPT_URI"] == "/cgi-bin/hello.rb"
			['200', {'Content-Type' => 'text/html'}, ["Migrated Hello World"]]
		else
			['200', {'Content-Type' => 'text/html'}, [
				"""
				#{ENV['SCRIPT_URL']}
				<br />
				#{ENV['QUERY_STRING']}

				"""
				]
			]
		end
	end
end

app = Rack::Builder.new do
  use Rack::CommonLogger
  use Rack::ShowExceptions
  run Dispatcher.new
end

Rack::Handler::CGI.run(app)
