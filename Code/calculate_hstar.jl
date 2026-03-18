using Oscar

#file = open("test.jl", "r")
t1 = time()
for i in 9:9
    open(string("julia_input/GTP", i, ".jl"), "r") do file_read
    open(string("julia_output/GTP", i, ".txt"), "w") do file_write
        t2 = time()
        println(string("Starting GTP", i))
	count = 1
        for line in eachline(file_read)
            println(string(count))
            line = strip(line)
            t3 = time()

            # Skip empty lines or comments
            if isempty(line) || startswith(line, "#")
                continue
            end

            # Evaluate the line (this will assign the variables)
            eval(Meta.parse(line))

            write(file_write, polytope)
            #println("A: ", A)
            #println("b: ", b)

            try
                    P = polyhedron(A,b)
                    dim_P = dim(P)
                if dim_P > 20 && dim_P < 22
                    h_star_eq = h_star_polynomial(P)
                    write(file_write, string(", ", h_star_eq, ", ", dim_P))
                else
                    write(file_write, string(", ", "Dimension too high", ", ", dim_P))
                end
            catch
                write(file_write, ", Unable to create polyhedron or calculate h*", ", NULL")
            end
            this_time = time() - t3
            total_this = time() - t2
            println(string("GTP", i, ", Time: ", this_time))
            println(string("Total time: ", total_this))
            write(file_write, string(", time: ", this_time, "s\n"))
            count = count + 1
        end
        elapsed_time = time() - t2
        total_time = time() - t1
        write(file_write, string("Total time (seconds): ", elapsed_time))
        println(string("Ending GTP", i, ", Running time (seconds): ", elapsed_time))
        println(string("Total time elapsed (seconds): ", total_time))
        println()
    end
    end

end
