def check_collateral_relevance(uploaded_file_asset) -> str:
    """Parses optional deck material context values passed by the user."""
    if uploaded_file_asset is not None:
        try:
            return uploaded_file_asset.read().decode("utf-8")
        except Exception:
            return "[Unable to convert file collateral context]"
    return ""
