from typing import Union


# note: we can get original_filename from cli ctx
def file_snapshot(original_filename: Union[str, None], prefix: str) -> None:
    """Create a snapshot of the given filename."""

    # prefix would be nice to include an id (e.g. translations_id)

    # concatenate file_id w/ original filename and save
    pass
