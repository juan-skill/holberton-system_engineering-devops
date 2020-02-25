#!/usr/bin/env ruby
# Find the regular expression that will match the above cases
puts ARGV[0].scan(/^h[0-9a-z]{1}n$/).join
