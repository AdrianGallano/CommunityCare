// import React, { useState, useEffect } from "react";
// import axios from "axios";

// const AddFamilyForm = ({ coordinates }) => {
//   const [formData, setFormData] = useState({
//     family_name: "",
//     street: "",
//     city: "",
//     state: "",
//     zipcode: "",
//     members: [],
//     latitude: "",
//     longitude: "",
//   });

//   const [memberData, setMemberData] = useState({
//     name: "",
//     age: "",
//     gender: "",
//     ethnicity: "",
//     occupation: "",
//     income: "",
//   });

//   useEffect(() => {
//     if (coordinates) {
//       setFormData((prevFormData) => ({
//         ...prevFormData,
//         latitude: coordinates.lat,
//         longitude: coordinates.lng,
//       }));
//     }
//   }, [coordinates]);

//   const handleChange = (e) => {
//     const { name, value } = e.target;
//     setFormData({ ...formData, [name]: value });
//   };

//   const handleMemberChange = (e) => {
//     const { name, value } = e.target;
//     setMemberData({ ...memberData, [name]: value });
//   };

//   const addMember = () => {
//     setFormData({
//       ...formData,
//       members: [...formData.members, { ...memberData, id: Date.now() }],
//     });
//     setMemberData({
//       name: "",
//       age: "",
//       gender: "",
//       ethnicity: "",
//       occupation: "",
//       income: "",
//     });
//   };

//   const handleSubmit = async (e) => {
//     e.preventDefault();
//     const newFamilyEntry = {
//       family_name: formData.family_name,
//       address: {
//         street: formData.street,
//         city: formData.city,
//         state: formData.state,
//         zipcode: formData.zipcode,
//       },
//       members: formData.members,
//       coordinates: {
//         latitude: Number(formData.latitude),
//         longitude: Number(formData.longitude),
//       },
//     };

//     try {
//       await axios.post("http://localhost:3000/family", newFamilyEntry);
//       alert("Family data added successfully!");
//       setFormData({
//         family_name: "",
//         street: "",
//         city: "",
//         state: "",
//         zipcode: "",
//         members: [],
//         latitude: "",
//         longitude: "",
//       });
//     } catch (error) {
//       console.error("Error adding family data:", error);
//     }
//   };

//   return (
//     <form onSubmit={handleSubmit}>
//       <h2>Add Family</h2>
//       <div>
//         <label>Family Name: </label>
//         <input
//           type="text"
//           name="family_name"
//           value={formData.family_name}
//           onChange={handleChange}
//           required
//         />
//       </div>
//       <div>
//         <label>Street: </label>
//         <input
//           type="text"
//           name="street"
//           value={formData.street}
//           onChange={handleChange}
//           required
//         />
//       </div>
//       <div>
//         <label>City: </label>
//         <input
//           type="text"
//           name="city"
//           value={formData.city}
//           onChange={handleChange}
//           required
//         />
//       </div>
//       <div>
//         <label>State: </label>
//         <input
//           type="text"
//           name="state"
//           value={formData.state}
//           onChange={handleChange}
//           required
//         />
//       </div>
//       <div>
//         <label>Zipcode: </label>
//         <input
//           type="text"
//           name="zipcode"
//           value={formData.zipcode}
//           onChange={handleChange}
//           required
//         />
//       </div>
//       <div>
//         <label>Latitude: </label>
//         <input
//           type="number"
//           name="latitude"
//           value={formData.latitude}
//           onChange={handleChange}
//           required
//           readOnly
//         />
//       </div>
//       <div>
//         <label>Longitude: </label>
//         <input
//           type="number"
//           name="longitude"
//           value={formData.longitude}
//           onChange={handleChange}
//           required
//           readOnly
//         />
//       </div>

//       <h3>Add Family Members</h3>
//       <div>
//         <label>Name: </label>
//         <input
//           type="text"
//           name="name"
//           value={memberData.name}
//           onChange={handleMemberChange}
//         />
//       </div>
//       <div>
//         <label>Age: </label>
//         <input
//           type="number"
//           name="age"
//           value={memberData.age}
//           onChange={handleMemberChange}
//         />
//       </div>
//       <div>
//         <label>Gender: </label>
//         <input
//           type="text"
//           name="gender"
//           value={memberData.gender}
//           onChange={handleMemberChange}
//         />
//       </div>
//       <div>
//         <label>Ethnicity: </label>
//         <input
//           type="text"
//           name="ethnicity"
//           value={memberData.ethnicity}
//           onChange={handleMemberChange}
//         />
//       </div>
//       <div>
//         <label>Occupation: </label>
//         <input
//           type="text"
//           name="occupation"
//           value={memberData.occupation}
//           onChange={handleMemberChange}
//         />
//       </div>
//       <div>
//         <label>Income: </label>
//         <input
//           type="number"
//           name="income"
//           value={memberData.income}
//           onChange={handleMemberChange}
//         />
//       </div>
//       <button type="button" onClick={addMember}>
//         Add Member
//       </button>

//       <h4>Members List</h4>
//       <ul>
//         {formData.members.map((member) => (
//           <li key={member.id}>
//             {member.name} - {member.age} - {member.gender}
//           </li>
//         ))}
//       </ul>

//       <button type="submit">Add Family</button>
//     </form>
//   );
// };

// export default AddFamilyForm;

import React, { useState, useEffect } from "react";
import axios from "axios";
import { Input } from "./ui/input";
import { Button } from "./ui/button";

const AddFamilyForm = ({ coordinates }) => {
  const [formData, setFormData] = useState({
    family_name: "",
    street: "",
    city: "",
    state: "",
    zipcode: "",
    members: [],
    latitude: "",
    longitude: "",
  });

  const [memberData, setMemberData] = useState({
    name: "",
    age: "",
    gender: "",
    ethnicity: "",
    occupation: "",
    income: "",
  });

  useEffect(() => {
    if (coordinates) {
      setFormData((prevFormData) => ({
        ...prevFormData,
        latitude: coordinates.lat,
        longitude: coordinates.lng,
      }));
    }
  }, [coordinates]);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleMemberChange = (e) => {
    const { name, value } = e.target;
    setMemberData({ ...memberData, [name]: value });
  };

  const addMember = () => {
    setFormData({
      ...formData,
      members: [...formData.members, { ...memberData, id: Date.now() }],
    });
    setMemberData({
      name: "",
      age: "",
      gender: "",
      ethnicity: "",
      occupation: "",
      income: "",
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const newFamilyEntry = {
      family_name: formData.family_name,
      address: {
        street: formData.street,
        city: formData.city,
        state: formData.state,
        zipcode: formData.zipcode,
      },
      members: formData.members,
      coordinates: {
        latitude: Number(formData.latitude),
        longitude: Number(formData.longitude),
      },
    };

    try {
      await axios.post("http://localhost:3000/family", newFamilyEntry);
      alert("Family data added successfully!");
      setFormData({
        family_name: "",
        street: "",
        city: "",
        state: "",
        zipcode: "",
        members: [],
        latitude: "",
        longitude: "",
      });
    } catch (error) {
      console.error("Error adding family data:", error);
    }
  };

  return (
    <>
      <form
        onSubmit={handleSubmit}
        className="m-4 grid grid-cols-2 gap-2 space-y-4 p-4 border rounded-md bg-gray-100"
      >
        <h2 className="col-span-2 text-xl font-bold">Add Family</h2>
        <div>
          <label className="block text-sm font-medium text-gray-700">
            Family Name
          </label>
          <Input
            type="text"
            name="family_name"
            value={formData.family_name}
            onChange={handleChange}
            required
            className="mt-1"
          />
        </div>
        <div>
          <label className="block text-sm font-medium text-gray-700">
            Street
          </label>
          <Input
            type="text"
            name="street"
            value={formData.street}
            onChange={handleChange}
            required
            className="mt-1"
          />
        </div>
        <div>
          <label className="block text-sm font-medium text-gray-700">
            City
          </label>
          <Input
            type="text"
            name="city"
            value={formData.city}
            onChange={handleChange}
            required
            className="mt-1"
          />
        </div>
        <div>
          <label className="block text-sm font-medium text-gray-700">
            State
          </label>
          <Input
            type="text"
            name="state"
            value={formData.state}
            onChange={handleChange}
            required
            className="mt-1"
          />
        </div>
        <div>
          <label className="block text-sm font-medium text-gray-700">
            Zipcode
          </label>
          <Input
            type="text"
            name="zipcode"
            value={formData.zipcode}
            onChange={handleChange}
            required
            className="mt-1"
          />
        </div>
        <div>
          <label className="block text-sm font-medium text-gray-700">
            Latitude
          </label>
          <Input
            type="number"
            name="latitude"
            value={formData.latitude}
            onChange={handleChange}
            required
            readOnly
            className="mt-1"
          />
        </div>
        <div>
          <label className="block text-sm font-medium text-gray-700">
            Longitude
          </label>
          <Input
            type="number"
            name="longitude"
            value={formData.longitude}
            onChange={handleChange}
            required
            readOnly
            className="mt-1"
          />
        </div>

        <h3 className="text-lg font-bold col-span-2">Add Family Members</h3>
        <div>
          <label className="block text-sm font-medium text-gray-700">
            Name
          </label>
          <Input
            type="text"
            name="name"
            value={memberData.name}
            onChange={handleMemberChange}
            className="mt-1"
          />
        </div>
        <div>
          <label className="block text-sm font-medium text-gray-700">Age</label>
          <Input
            type="number"
            name="age"
            value={memberData.age}
            onChange={handleMemberChange}
            className="mt-1"
          />
        </div>
        <div>
          <label className="block text-sm font-medium text-gray-700">
            Gender
          </label>
          <Input
            type="text"
            name="gender"
            value={memberData.gender}
            onChange={handleMemberChange}
            className="mt-1"
          />
        </div>
        <div>
          <label className="block text-sm font-medium text-gray-700">
            Ethnicity
          </label>
          <Input
            type="text"
            name="ethnicity"
            value={memberData.ethnicity}
            onChange={handleMemberChange}
            className="mt-1"
          />
        </div>
        <div>
          <label className="block text-sm font-medium text-gray-700">
            Occupation
          </label>
          <Input
            type="text"
            name="occupation"
            value={memberData.occupation}
            onChange={handleMemberChange}
            className="mt-1"
          />
        </div>
        <div>
          <label className="block text-sm font-medium text-gray-700">
            Income
          </label>
          <Input
            type="number"
            name="income"
            value={memberData.income}
            onChange={handleMemberChange}
            className="mt-1"
          />
        </div>
        <Button type="button" onClick={addMember} className="mt-2">
          Add Member
        </Button>

        <Button type="submit" className="mt-4">
          Add Family
        </Button>

        <h4 className="text-lg font-bold mt-4">Members List</h4>
        <ul className="list-disc pl-5">
          {formData.members.map((member) => (
            <li key={member.id}>
              {member.name} - {member.age} - {member.gender}
            </li>
          ))}
        </ul>
      </form>
    </>
  );
};

export default AddFamilyForm;
