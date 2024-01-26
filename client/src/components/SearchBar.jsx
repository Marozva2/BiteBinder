import React, { useState } from "react";

const SearchBar = ({ onSearch }) => {
  const [searchInput, setSearchInput] = useState("");

  const handleSearch = () => {
    onSearch(searchInput);
  };

  return (
    <div>
      <div className="ui large fluid icon input">
        <input
          type="text"
          placeholder="Enter an ingredient"
          value={searchInput}
          onChange={(e) => setSearchInput(e.target.value)}
        />
        <button className="ui primary button" onClick={handleSearch}>
          Search
        </button>
      </div>
      <div>
        <h1>Your search results:</h1>
      </div>
    </div>
  );
};

export default SearchBar;
