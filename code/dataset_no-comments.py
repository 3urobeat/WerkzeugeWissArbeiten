from __future__ import annotations

from typing import Union, List, Tuple, Any, Callable
from abc import ABC, abstractmethod

class DataSetItem():

	def __init__(self, name:str, id:int, content:Any):
		if not isinstance(name, str) or not isinstance(id, int):
			raise TypeError("A DataSetItem requires the name to be a str and the id to be an int!")
			
		self.name = name 
		self.id = id 
		self.content = content

	def __str__(self):
		return "Item {name} ({id}) containing {t}{p}".format(
				name=self.name, id=self.id,
				t=type(self.content).__name__,
				p=" ("+self.content[:10]+"...)" if isinstance(self.content, str) else "" 
			)

class DataSetInterface(ABC):

	ITERATE_SORT_BY_NAME = "name"
	ITERATE_SORT_BY_ID = "id"

	def __init__(self, items:Union[List[DataSetItem], Tuple[DataSetItem, ...]]=[]):
		self.iterate_sorted = True 
		self.iterate_reversed = False 
		self.iterate_key = self.ITERATE_SORT_BY_NAME

	def set_iteration(self, sort=None, reverse=None, key=None):
		if sort is not None:
			self.iterate_sorted = bool(sort)
		if reverse is not None:
			self.iterate_reversed = bool(reverse)
		if key is not None:
			self.iterate_key = self.ITERATE_SORT_BY_ID if key == self.ITERATE_SORT_BY_ID else self.ITERATE_SORT_BY_NAME

	@abstractmethod
	def __setitem__(self, name:str, id_content:Tuple[int, Any]):
		pass

	@abstractmethod
	def __iadd__(self, item:DataSetItem):
		pass

	@abstractmethod
	def __delitem__(self, name:str):
		pass

	@abstractmethod
	def __contains__(self, name:str) -> bool:
		pass

	@abstractmethod
	def __getitem__(self, name:str) -> DataSetItem:
		pass

	@abstractmethod
	def __and__(self, dataset:DataSetInterface) -> DataSetInterface:
		pass

	@abstractmethod
	def __or__(self, dataset:DataSetInterface) -> DataSetInterface:
		pass

	@abstractmethod
	def __iter__(self):
		pass

	@abstractmethod
	def filtered_iterate(self, filter:Callable[[str, int], bool]):
		pass 

	@abstractmethod
	def __len__(self) -> int:
		pass	

	def __str__(self):
		return  "DataSet mit {n} Elementen:\n\t - {items}".format(
			n=len(self),
			items='\n\t - '.join([str(i) for i in self])
		)
			
