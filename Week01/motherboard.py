class Motherboard:
    """
    The motherboard class is an object containing various attributes related to a motherboard.
    """
    def __init__( self, name = str, cpu_socket = str, ram_slots = int, ram_max = int, pci_express_slots = int, sata_slots = int, m2_slots = int ):
        """
        Initialize the motherboard class.
        
        name (str): The name of the motherboard.
        cpu_socket (str): The CPU socket type.
        ram_slots (int): The number of RAM slots on the motherboard.
        ram_max (int): The maximum amount of RAM supported by the motherboard in GB.
        pci_express_slots (int): The number of PCIex16 slots on the motherboard.
        sata_slots (int): The number of SATA slots on the motherboard.
        m2_slots (int): The number of M.2 slots on the motherboard.
        """
        self.motherboard = name
        self.cpu_socket = cpu_socket
        self.ram_slots = ram_slots
        self.ram_max = ram_max
        self.pci_express_slots = pci_express_slots
        self.sata_slots = sata_slots
        self.m2_slots = m2_slots

    def add_cpu( self, cpu = str, socket_type = str, ram_type = str, ram_speed = int ):
        """
        Add a CPU to the motherboard.
       
        cpu (str): The name of the CPU.
        socket_type (str): The CPU socket type.
        ram_type (str): The RAM type supported by the CPU.
        ram_speed (int): The max RAM speed supported by the CPU.
        """
        if not 'cpu' in self.__dict__ and socket_type == self.cpu_socket:
            self.cpu = cpu
            self.ram_support = [ ram_type, ram_speed ]
            return True
        else:
            print( "CPU not compatible with motherboard!" )
    
    def add_ram( self, ram_type = str, ram_memory = int, ram_speed = int, ram_count = int ):
        """
        Add RAM to the motherboard.
        
        ram_type (str): The RAM type.
        ram_memory (int): The amount of RAM per module in GB.
        ram_speed (int): The RAM speed.
        ram_count (int): The number of RAM modules.
        """
        if not 'ram' in self.__dict__ and ram_type in self.ram_support and ram_count <= self.ram_slots and ram_memory * ram_count <= self.ram_max:
            if self.ram_support[ 1 ] < ram_speed:
                print( "RAM speed is greater than the max supported by the CPU, it will be reduced to the max supported speed!" )
                self.ram = f"{ ram_memory }GBx{ ram_count } { ram_type }-{ self.ram_support[ 1 ] }"
            else:
                self.ram = f"{ ram_memory }GBx{ ram_count } { ram_type }-{ ram_speed }"
            return True
        else:
            print( "RAM not compatible with motherboard!" )
            return False
    
    def add_gpu( self, gpu = str, gpu_memory_type = str, gpu_memory = int, gpu_count = int ):
        """
        Add a GPU to the motherboard.
        
        gpu (str): The name of the GPU.
        gpu_memory_type (str): The GPU memory type.
        gpu_memory (int): The amount of GPU memory in GB.
        gpu_count (int): The number of GPUs.
        """
        if not 'gpu' in self.__dict__ and gpu_count <= self.pci_express_slots:
            self.gpu = f"{ gpu } { gpu_memory_type } { gpu_memory }GB x{ gpu_count }"
            return True
        else:
            print( "GPU not compatible with motherboard!" )
            return False
    
    def add_storage( self, storage_name = str, storage_space = int, storage_count = int ):
        """
        Add storage to the motherboard.
        
        storage_name (str): The name of the storage device.
        storage_space (int): The amount of storage space in GB.
        storage_count (int): The number of storage devices.
        """
        if not 'storage' in self.__dict__ and storage_count <= self.sata_slots + self.m2_slots:
            self.storage = f"{ storage_name } { storage_space }GB x{ storage_count }"
            return True
        else:
            print( "Storage not compatible with motherboard!" )
            return False