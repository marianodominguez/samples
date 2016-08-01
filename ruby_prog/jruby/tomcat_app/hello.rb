require 'rubygems'
require 'sinatra'
require 'sinatra/reloader' if development?

get '/' do
	@message = "Hello, world! from Sinatra running JRuby on Tomcat"
	erb :index
end
