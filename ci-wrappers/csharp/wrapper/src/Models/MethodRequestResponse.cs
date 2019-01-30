/*
 * IoT SDK Device & Client REST API
 *
 * REST API definition for End-to-end testing of the Azure IoT SDKs.  All SDK APIs that are tested by our E2E tests need to be defined in this file.  This file takes some liberties with the API definitions.  In particular, response schemas are undefined, and error responses are also undefined.
 *
 * OpenAPI spec version: 1.0.0
 * 
 * Generated by: https://github.com/swagger-api/swagger-codegen.git
 */

using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Collections;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.ComponentModel.DataAnnotations;
using System.Runtime.Serialization;
using Newtonsoft.Json;

namespace IO.Swagger.Models
{ 
    /// <summary>
    /// result of waiting on a method call
    /// </summary>
    [DataContract]
    public partial class MethodRequestResponse : IEquatable<MethodRequestResponse>
    { 
        /// <summary>
        /// payload for the request that arrived from the service
        /// </summary>
        /// <value>payload for the request that arrived from the service</value>
        [DataMember(Name="requestPayload")]
        public Object RequestPayload { get; set; }

        /// <summary>
        /// response ID to be used when responding to this method call
        /// </summary>
        /// <value>response ID to be used when responding to this method call</value>
        [DataMember(Name="responseId")]
        public string ResponseId { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class MethodRequestResponse {\n");
            sb.Append("  RequestPayload: ").Append(RequestPayload).Append("\n");
            sb.Append("  ResponseId: ").Append(ResponseId).Append("\n");
            sb.Append("}\n");
            return sb.ToString();
        }

        /// <summary>
        /// Returns the JSON string presentation of the object
        /// </summary>
        /// <returns>JSON string presentation of the object</returns>
        public string ToJson()
        {
            return JsonConvert.SerializeObject(this, Formatting.Indented);
        }

        /// <summary>
        /// Returns true if objects are equal
        /// </summary>
        /// <param name="obj">Object to be compared</param>
        /// <returns>Boolean</returns>
        public override bool Equals(object obj)
        {
            if (ReferenceEquals(null, obj)) return false;
            if (ReferenceEquals(this, obj)) return true;
            return obj.GetType() == GetType() && Equals((MethodRequestResponse)obj);
        }

        /// <summary>
        /// Returns true if MethodRequestResponse instances are equal
        /// </summary>
        /// <param name="other">Instance of MethodRequestResponse to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(MethodRequestResponse other)
        {
            if (ReferenceEquals(null, other)) return false;
            if (ReferenceEquals(this, other)) return true;

            return 
                (
                    RequestPayload == other.RequestPayload ||
                    RequestPayload != null &&
                    RequestPayload.Equals(other.RequestPayload)
                ) && 
                (
                    ResponseId == other.ResponseId ||
                    ResponseId != null &&
                    ResponseId.Equals(other.ResponseId)
                );
        }

        /// <summary>
        /// Gets the hash code
        /// </summary>
        /// <returns>Hash code</returns>
        public override int GetHashCode()
        {
            unchecked // Overflow is fine, just wrap
            {
                var hashCode = 41;
                // Suitable nullity checks etc, of course :)
                    if (RequestPayload != null)
                    hashCode = hashCode * 59 + RequestPayload.GetHashCode();
                    if (ResponseId != null)
                    hashCode = hashCode * 59 + ResponseId.GetHashCode();
                return hashCode;
            }
        }

        #region Operators
        #pragma warning disable 1591

        public static bool operator ==(MethodRequestResponse left, MethodRequestResponse right)
        {
            return Equals(left, right);
        }

        public static bool operator !=(MethodRequestResponse left, MethodRequestResponse right)
        {
            return !Equals(left, right);
        }

        #pragma warning restore 1591
        #endregion Operators
    }
}