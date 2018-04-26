<?php
// using Trait technical
// we even don't need this
public abstract class Vehicle {
    public function go();
}

Trait GoByDrivingAlgorithm {
    public function go() {
        echo 'I am driving.';
    }
}

class StreetRacer {
    use GoByDrivingAlgorithm;
}
