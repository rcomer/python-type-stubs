from typing import Optional, Tuple, Any, overload, IO

from pygame.event import Event
from . import music as music
import numpy
@overload  # do we need this overloads for None = None?
def init(
    frequency: Optional[int] = 44100,
    size: Optional[int] = -16,
    channels: Optional[int] = 2,
    buffer: Optional[int] = 512,
    devicename: Optional[str] = None,
    allowedchanges: Optional[int] = 5,
) -> None: ...
@overload
def init(
    frequency: Optional[int] = 44100,
    size: Optional[int] = -16,
    channels: Optional[int] = 2,
    buffer: Optional[int] = 512,
    devicename: Optional[None] = None,
    allowedchanges: Optional[int] = 5,
) -> None: ...
@overload  # do we need this overloads for None = None?
def pre_init(
    frequency: Optional[int] = 44100,
    size: Optional[int] = -16,
    channels: Optional[int] = 2,
    buffer: Optional[int] = 512,
    devicename: Optional[str] = None,
) -> None: ...
@overload
def pre_init(
    frequency: Optional[int] = 44100,
    size: Optional[int] = -16,
    channels: Optional[int] = 2,
    buffer: Optional[int] = 512,
    devicename: Optional[None] = None,
) -> None: ...
def quit() -> None: ...
def get_init() -> Tuple[int, int, int]: ...
def stop() -> None: ...
def pause() -> None: ...
def unpause() -> None: ...
def fadeout(time: int) -> None: ...
def set_num_channels(count: int) -> None: ...
def get_num_channels() -> int: ...
def set_reserved() -> None: ...
def find_channel(force: bool) -> Channel: ...
def get_busy() -> bool: ...
def get_sdl_mixer_version(linked: bool) -> Tuple[int, int, int]: ...

class Sound:
    @overload
    def __init__(self, file: IO) -> None: ...
    @overload
    def __init__(self, buffer: Any) -> None: ...  # Buffer protocol is still not implemented in typing
    @overload
    def __init__(self, array: numpy.ndarray) -> None: ...  # Buffer protocol is still not implemented in typing
    def play(self, loops: Optional[int] = 0, maxtime: Optional[int] = 0, fade_ms: Optional[int] = 0) -> Channel: ...
    def stop(self) -> None: ...
    def fadeout(self, time: int) -> None: ...
    def set_volume(self, value: float) -> None: ...
    def get_volume(self) -> float: ...
    def get_num_channels(self) -> int: ...
    def get_length(self) -> float: ...
    def get_raw(self) -> bytes: ...

class Channel:
    def __init__(self, id: int) -> None: ...
    def play(self, sound: Sound, loops: Optional[int] = 0, maxtime: Optional[int] = 0, fade_ms: Optional[int] = 0) -> None: ...
    def stop(self) -> None: ...
    def pause(self) -> None: ...
    def unpause(self) -> None: ...
    def fadeout(self, time: int) -> None: ...
    @overload
    def set_volume(self, value: float) -> None: ...
    @overload
    def set_volume(self, left: float, right: float) -> None: ...
    def get_volume(self) -> float: ...
    def get_busy(self) -> bool: ...
    def get_sound(self) -> Sound: ...
    def get_queue(self) -> Sound: ...
    @overload
    def set_endevent(self, type: Optional[int] = None) -> None: ...
    @overload
    def set_endevent(self, type: Optional[Event] = None) -> None: ...
    def get_endevent(self) -> int: ...

