def ip_in_range(ip)
  return true
end

file_name = "input.txt"
times = ARGV[2] || 1

lines_processed = Hash.new

File.open(file_name, "r").each_line do |line|
  if(ip_in_range(line))
  	result = `ping -c #{times} #{line}`
  	puts "Result nil? #{result.nil?}"
  	puts "Result empty? #{result.empty?}"
  	lines_processed[line] = !result.nil? && !result.empty?
  	puts "Ping to #{line} with result #{lines_processed[line]}"
  end
  #result = `ping -c #{times} #{line} ; echo $?`
end

puts "Results: \n#{lines_processed}"
