Warbler::Config.new do |config|
  config.jar_name = "hello"
  config.dirs     = %w(views)
  config.includes = FileList["hello.rb"]
  config.gems     = ["sinatra"]
end