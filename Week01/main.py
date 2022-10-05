from motherboard import Motherboard

def main(  ):

    # Create a new motherboard object with specific specs and print the info for the user.
    mobo = Motherboard( name = "ASUS ROG STRIX B550 GAMING", cpu_socket = "AM4", ram_slots = 4, ram_max = 128, pci_express_slots = 2, sata_slots = 6, m2_slots = 2 )
    print( f"You have the { mobo.motherboard } motherboard supporting a CPU with the { mobo.cpu_socket } socket type.\nThe motherboard has { mobo.ram_slots } RAM slots supporting a maximum of { mobo.ram_max }GB of memory.\nit also has { mobo.pci_express_slots } PCIex16 slots for adding GPUs, { mobo.sata_slots } SATA slots, and { mobo.m2_slots } M.2 slots.\n" )
    
    uin = input( "Would you like to add components to the motherboard? (y/n): " )
    if ( uin == "y" ):
        # Add a CPU to the motherboard with various user inputs as the parameters or exit if it's incompatible.
        if mobo.add_cpu( input( "Enter the CPU name: " ), input( "Enter the CPU socket type: " ), input( "Enter the supported RAM type: " ), int( input( "Enter the max supported RAM speed: " ) ) ):
            print( f"CPU { mobo.cpu } added to motherboard!\n" )
        else:
            print( "CPU not added to motherboard!\n" )
            return
        
        # Add RAM to the motherboard with various user inputs as the parameters or exit if it's incompatible.
        if mobo.add_ram( input( "Enter the RAM type: " ), int( input( "Enter the RAM memory: " ) ), int( input( "Enter the RAM speed: " ) ), int( input( "Enter the RAM module count: " ) ) ):
            print( f"RAM { mobo.ram } added to motherboard!\n" )
        else:
            print( "RAM not added to motherboard!\n" )
            return
        
        # Add a GPU to the motherboard with various user inputs as the parameters or exit if it's incompatible.
        if mobo.add_gpu( input( "Enter the GPU name: " ), input( "Enter the GPU memory type: " ), int( input( "Enter the GPU memory: " ) ), int( input( "Enter the GPU count: " ) ) ):
            print( f"GPU { mobo.gpu } added to motherboard!\n" )
        else:
            print( "GPU not added to motherboard!\n" )
            return

        # Add storage to the motherboard with various user inputs as the parameters or exit if it's incompatible.
        if mobo.add_storage( input( "Enter the storage name: " ), int( input( "Enter the storage space: " ) ), int( input( "Enter the storage count: " ) ) ):
            print( f"Storage { mobo.storage } added to motherboard!\n" )
        else:
            print( "Storage not added to motherboard!\n" )
            return
        
        # Print the final system specs.
        print( f"Your { mobo.motherboard } motherboard has the { mobo.cpu_socket } socket filled with the { mobo.cpu } CPU,\n{ mobo.ram_slots } RAM slots filled with { mobo.ram } memory out of { mobo.ram_max }GB max supported,\n{ mobo.pci_express_slots } PCIex16 slots filled with { mobo.gpu } GPU(s),\nand { mobo.m2_slots } M.2 Slots filled with { mobo.storage }!" )
    else:
        print( "Okay fine then..." )

if __name__ == "__main__":
    main(  )