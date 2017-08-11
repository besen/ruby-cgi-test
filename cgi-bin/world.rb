#!/home/besen/.rvm/rubies/ruby-2.3.3/bin/ruby
     
require 'cgi'
cgi = CGI.new
print cgi.header
 
print "World!\n"