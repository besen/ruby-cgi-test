#!/home/besen/.rvm/wrappers/ruby-2.3.3/ruby

require 'rubygems'
require 'bundler/setup'
require "rack"

require_relative "../app/new-app.rb"

app = Rack::Builder.new do
  use Rack::CommonLogger
  use Rack::ShowExceptions
  run NewApp.new
end

Rack::Handler::CGI.run(app)
