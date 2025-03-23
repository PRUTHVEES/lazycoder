<?php

class Profile {
    
    public $name;
    
    public $email;
    
    public $age;
    

    public function __construct($name, $email, $age) {
        
        $this->name = $name;
        
        $this->email = $email;
        
        $this->age = $age;
        
    }

    public function display() {
        echo "Class Profile: ";
        
        echo "name = " . $this->name . " ";
        
        echo "email = " . $this->email . " ";
        
        echo "age = " . $this->age . " ";
        
    }
}
?>