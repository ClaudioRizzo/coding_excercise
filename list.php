<?php

class Node {
	private $next = NULL;
	private $data = NULL;

	function __construct($data) {
		$this->data = $data;
	}

	function next() {
		return $this->next;
	}

	function setNext($next) {
		$this->next = $next;
	}

	function getData() {
		return $this->data;
	}
}

class SingleList {
	private $head = NULL;
	private $size = 0;

	function __construct($head) {
		if($head !== NULL) {
			$this->head = $head;
			$this->size += 1;
		}
	}

	function append($node) {
		
		if($this->head === NULL) {
			$this->head = $node;
		} else {
			$current = $this->head;
			while($current->next() != NULL) {
				$current = $current->next();
			}

			$current->setNext($node);
		}
		
		$this->size += 1;
	}

	function getSize() {
		return $this->size;
	}

	function getAt($index){
		if($index >= $this->size || $index < 0) {
			echo "Index out of range";
		} else {

			$current = $this->head;
			for($i=0; $i<$index; $i++) {
				$current = $current->next();
			}
			return $current;
		}
	}

	function insertAt($node, $index) {
		if($index > $this->size || $index < 0) {
			echo "Index out of range";
		} else if( $index === $this->size) {
			$this->append($node);
		} else if($index === 0) {
			$node->setNext($this->head);
			$this->head = $node;
			$this->size += 1;
		} else {
			$current = $this->head;
			for($i=0; $i<$index-1; $i++) {
				$current = $current->next();
			}
			$tmp = $current->next();
			$current->setNext($node);
			$node->setNext($tmp);
			$this->size+=1;
		}
	}
}

$n = new Node(4);
$l = new SingleList(NULL);
echo $l -> getSize();
$l->insertAt(new Node(5), 0);

echo $l -> getSize();
echo $l->getAt(0)->getData();

?>
